from pathlib import Path
import re

noteshapes = [
    'X', 'L', 'S', 's', 'M', 'm', 'U', 'u',
    'X.', 'L.', 'S.', 's.', 'M.', 'm.', 'U.',
    '*custos'
]
ligatures = ['[', ']']
accids = ['#', '-']
pitches = [
    'r',
    'CC', 'DD', 'EE', 'FF', 'GG', 'AA', 'BB',
    'C', 'D', 'E', 'F', 'G', 'A', 'B',
    'c', 'd', 'e', 'f', 'g', 'a', 'b',
    'cc', 'dd', 'ee', 'ff', 'gg', 'aa', 'bb',
]
rest_lines = ['_1', '_2', '_3', '_4', '_5']

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

pattern = re.compile(
    rf'(?P<ligature_start>{ligature_pattern})?'
    rf'(?P<shape>{shape_pattern})'
    rf'(?P<pitch>{pitch_pattern})'
    rf'(?P<restline>{restline_pattern})?'
    rf'(?P<accidental>{accid_pattern})?'
    rf'(?P<ligature_end>{ligature_pattern})?'
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


input_dir = Path("samples")
for file_path in samples_dir.rglob("*.lmx"):
    with file_path.open("r", encoding="utf-8") as infile_mensstaff:
        lines = infile_mensstaff.readlines()

    with file_path.open("w", encoding="utf-8") as outfile_subtokenized:
        for line in lines:
            mens_token = line.stip()
            components = tokenize(mens_token)
            outfile_subtokenized.write(" ".join(components) + "\n")
    print(f"Processed: {file_path}")