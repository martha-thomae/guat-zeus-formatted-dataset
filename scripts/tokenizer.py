from pathlib import Path
import re

noteshapes = [
    'X', 'L', 'S', 's', 'M', 'm', 'U', 'u',
    '*custos'
]
ligatures = ['[', ']']
accids = [
    '#', '-', 'n', 
    '#y', '-y', 'ny', 
    '#X', '-X', 'nX', 
    'yy', '-yy', 'X#',
    'X-', 'Xn',
    'y#', 'y-', 'yn',
    '#yy', 'nyy',
    '#XX', '-XX', 'nXX',
    '#xx', '-xx', 'nxx',
    'y']
pitches = [
    'r',
    'CC', 'DD', 'EE', 'FF', 'GG', 'AA', 'BB',
    'C', 'D', 'E', 'F', 'G', 'A', 'B',
    'c', 'd', 'e', 'f', 'g', 'a', 'b',
    'cc', 'dd', 'ee', 'ff', 'gg', 'aa', 'bb',
]
rest_lines = ['_1', '_2', '_3', '_4', '_5']
beams = ['(', ')']
color = ['~']
fermata = [';']
stems = ['/', '\\']
dots = [':']

def make_pattern(items):
    return '|'.join(
        re.escape(item)
        for item in sorted(items, key=len, reverse=True)
    )

shape_pattern = make_pattern(noteshapes)
pitch_pattern = make_pattern(pitches)
ligature_pattern = make_pattern(ligatures)
accid_pattern = make_pattern(accids)
restline_pattern = make_pattern(rest_lines)
beamed_pattern = make_pattern(beams)
coloration_pattern = make_pattern(color)
fermata_pattern = make_pattern(fermata)
stemdir_pattern = make_pattern(stems)
dot_pattern = make_pattern(dots)

pattern = re.compile(
    rf'(?P<ligature_start>{ligature_pattern})?'
    rf'(?P<shape>{shape_pattern})'
    rf'(?P<dot>{dot_pattern})?'
    rf'(?P<color>{coloration_pattern})?'
    rf'(?P<pitch>{pitch_pattern})'
    rf'(?P<restline>{restline_pattern})?'
    rf'(?P<accidental>{accid_pattern})?'
    rf'(?P<stem>{stemdir_pattern})?'
    rf'(?P<fermata>{fermata_pattern})?'
    rf'(?P<ligature_end>{ligature_pattern})?'
    rf'(?P<beam>{beamed_pattern})?'
)

def tokenize(mens_token):
    match = pattern.fullmatch(mens_token)

    if not match:
        return [mens_token]

    return [
        value
        for value in match.groups()
        if value is not None
    ]


input_dir = Path(input("ENTER the SAMPLES FOLDER for all the samples (encoded in **mens but stored as .lmx) that you would want to sub-tokenize: "))
for file_path in input_dir.rglob("*.lmx"):
    with file_path.open("r", encoding="utf-8") as infile_mensstaff:
        lines = infile_mensstaff.readlines()

    with file_path.open("w", encoding="utf-8") as outfile_subtokenized:
        for line in lines:
            mens_token = line.strip()
            components = tokenize(mens_token)
            outfile_subtokenized.write(" ".join(components) + "\n")
    print(f"Processed: {file_path}")

# Error in: guat-zeus-formatted-dataset/samples/01_Asperges-me/Folio2r_Region25094.lmx ('Mfy', the 'y' with no accidental, whould be '#y')
# Error in: guat-zeus-formatted-dataset/samples/10_Missa-TorresyMartinezBravo/Folio72r_Region35190.lmx and Folio79r_Region35315.lmx ('MByy', should be 'MBn X?')