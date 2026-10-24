from pathlib import Path

predictions_filepath = input("Enter the file path: ")
# predictions_filepath = "3) EXPERIMENT 3 - no stemdir + sub-tokenized (SER 3.0 | vocab 92)/out/evaluation/predictionsBackToMens.lmx"
# predictinos_filepath = "2) EXPERIMENT 2 - no stemdir (SER 12.1 | vocab 667)/out/evaluation/predictions.lmx"
# "0) reference/groundtruth.testNoStemDir.txt"
# "5) ReRunExperiments - TRUE MENS (tokens & subtokens)/groundtruth.fulltokens.test.lmx"

try:
    with open(predictions_filepath, "r", encoding="utf-8") as predictions_file:
        lines = predictions_file.readlines()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

file_path = Path(predictions_filepath)
directory_path = file_path.parent

for n, prediction_line in enumerate(lines):
    prediction_line = prediction_line.replace('.', ':')
    result = "**mens\n" + "\n".join(prediction_line.split())
    print(result)
    new_filename = "out" + str(n+1) + ".txt"
    new_file_path = directory_path / "mensfiles" / new_filename
    with open(new_file_path, "w", encoding="utf-8") as outfile:
        outfile.write(result)
    print()
