import re

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

for folder in directory.iterdir():
    if folder.is_dir():
        #print(f"Folder: {folder.name}")
        for file in folder.iterdir():
            if file.is_file() and file.suffix == ".lmx":
                #print(f". File: {file.name}")
                with file.open("r", encoding="utf-8") as infile:
                    content = infile.readlines()

                clef = content[0].rstrip('\n')
                pitches_above_line3 = default_stemdown_pitches[clef]
                for line in content[1:]:
                    if downstem_char in line:
                        pitch = find_pitch_subtoken(line)
                        if pitch in pitches_above_line3:
                            print(pitch, downstem_char, "remove")
                            remove(downstem_char) # in this case, the encoding of the stem direction is redundant  #DEFINE FUNCTION
                        else:
                            print(pitch, downstem_char, "preserve")
                            pass # leave the stem, as it indicates something different from the default
                    elif upstem_char in line:
                        pitch = find_pitch_subtoken(line)
                        if pitch in pitches_above_line3:
                            print(pitch, upstem_char, "preserve")
                            pass # leave the stem, as it indicates something different from the default
                        else:
                            print(pitch, upstem_char, "remove")
                            remove(upstem_char) # in this case, the encoding of the stem direction is redundant 
