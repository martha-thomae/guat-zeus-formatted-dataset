from pathlib import Path
#line = "*clefC4 M. B - m B M B M G [ s A s B ] s G s d M e M e M e M e s f s e S d s B M r _4 M c M c M. c m c M B M c s A M G s E *custos A"

input_file = Path("./predictions.lmx")
output_file = Path("./predictionsBackToMens.lmx")
with input_file.open("r", encoding="utf-8") as infile, \
    output_file.open("w", encoding="utf-8") as outfile:

    for line in infile:
        menstoken_list = []
        menstoken = ""
        for subtoken in line.split():
            if subtoken in ['[', '*custos', '=='] or ('*met(' in subtoken) or ('*k[' in subtoken): # Start ligature
                menstoken_list.append(menstoken)
                menstoken = subtoken
            elif subtoken in ['L', 'S', 's', 'M', 'm', 'U', 'u', 'L.', 'S.', 's.', 'M.', 'm.', 'U.']: # Note shape
                if menstoken == '[': # Following the start of a ligature
                    menstoken += subtoken
                else: # New note not following a ligature start, then beginning of new token in **mens
                    menstoken_list.append(menstoken)
                    menstoken = subtoken
            else:
                menstoken += subtoken
        menstoken_list.append(menstoken)
        print(menstoken_list)

        if 'L' in menstoken_list: #As a single token
            print(True)
            index = menstoken_list.index('L')
            menstoken_list[index-1] = menstoken_list[index-1] + 'L'
            del menstoken_list[index]

        outfile.write(" ".join(menstoken_list) + "\n")
