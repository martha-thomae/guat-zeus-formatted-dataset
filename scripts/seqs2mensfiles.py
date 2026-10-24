from pathlib import Path

predictions_filepath = input("Enter the file path: ")
# file path to "predictionsBackToMens.lmx" or to "predictions.lmx" or to "groundtruth.fulltokens.test.lmx"

try:
    with open(predictions_filepath, "r", encoding="utf-8") as predictions_file:
        lines = predictions_file.readlines()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

file_path = Path(predictions_filepath)
directory_path = file_path.parent

# Create the mensfiles directory if it doesn't exist
(file_path.parent / "mensfiles").mkdir(parents=True, exist_ok=True)

for n, prediction_line in enumerate(lines):
    prediction_line = prediction_line.replace('.', ':')
    result = "**mens\n" + "\n".join(prediction_line.split())
    print(result)

    new_filename = "out" + str(n+1) + ".txt"
    new_file_path = directory_path / "mensfiles" / new_filename

    with open(new_file_path, "w", encoding="utf-8") as outfile:
        outfile.write(result)

    print()
