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
    # if match:
    #     return match.groupdict()
    # return {'unmatched': mens_token}

input_file = Path("./samples/01_Asperges-me/Folio1v_Region25073.lmx")
output_file = Path("./example-of-tokenizer/Folio1v_Region25073_SUBTOKENIZED.lmx")

with input_file.open("r", encoding="utf-8") as infile_mensstaff, \
     output_file.open("w", encoding="utf-8") as outfile_subtokenized:

    for line in infile_mensstaff:
        mens_token = line.strip()
        components = tokenize(mens_token)

        outfile_subtokenized.write(" ".join(components) + "\n")
