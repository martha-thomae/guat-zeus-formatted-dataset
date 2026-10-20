import re
from pathlib import Path

downstem_char = "\\"
upstem_char = "/"

pitches = ["CC", "DD", "EE", "FF", "GG", "AA", "BB",
    "C", "D", "E", "F", "G", "A", "B", 
    "c", "d", "e", "f", "g", "a", "b", 
    "cc", "dd", "ee", "ff", "gg", "aa", "bb"
]

# Guatemala's clefs: "C1", "C2", "C3", "C4" \ "F3", "F4" \ "G2"
default_stemdown_pitches = {
    "*clefC1": pitches[19:27],
    "*clefC2": pitches[17:25],
    "*clefC3": pitches[15:23],
    "*clefC4": pitches[13:21],
    "*clefC5": pitches[11:19],
    "*clefF1": pitches[15:23],
    "*clefF2": pitches[13:21],
    "*clefF3": pitches[11:19],
    "*clefF4": pitches[9:17],
    "*clefF5": pitches[7:15],
    "*clefG2": pitches[21:29]
} # from space 3 (to an octave above), the pitches are supposed
  # to have a stem on the downward direction (\) by default

pattern = re.compile("|".join(re.escape(p) for p in sorted(pitches, key=len, reverse=True)))
def find_pitch_subtoken(line):
    match = pattern.search(line)
    return match.group() if match else None

directory = Path("samples/")
# Get the content of the files
for folder in directory.iterdir():
    if folder.is_dir():
        print(f"Folder: {folder.name}")
        for file in folder.iterdir():
            if file.is_file() and file.suffix == ".lmx":                
                with file.open("r", encoding="utf-8") as infile:
                    inlines = infile.readlines()

                # Find the clef and, with it, determine the pitches above the third line,
                # as these are the ones where the default stem direction changes
                clef = inlines[0].rstrip('\n')
                pitches_above_line3 = default_stemdown_pitches[clef]

                # Write a new file with the stem direction information cleand up
                # i.e., removing redundant stem direction information, which means that 
                # the stem direction is only provided when it is opposite to the default
                with file.open("w", encoding="utf-8") as outfile:
                    for line in inlines:
                        if downstem_char in line:
                            pitch = find_pitch_subtoken(line)
                            if pitch in pitches_above_line3:
                                # Remove the downward stem as it is redundant information
                                line = line.replace(downstem_char, "")
                            else:
                                # Leave the (downward) stem, as it indicates something different from the default
                                pass
                        elif upstem_char in line:
                            pitch = find_pitch_subtoken(line)
                            if pitch in pitches_above_line3:
                                # Leave the (upward) stem, as it indicates something different from the default
                                pass
                            else:
                                # Remove the upward stem as it is redundant information
                                line = line.replace(upstem_char, "") # in this case, the encoding of the stem direction is redundant 
                        outfile.write(line)
                print(f". File: {file.name} -> Processed")
