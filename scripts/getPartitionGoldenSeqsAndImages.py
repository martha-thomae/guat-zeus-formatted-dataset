# Get a samples file (txt format) listing the path to all the samples in the partition
# (either train, dev, or test partition) and return a LMX file that includes the GOLDEN sequence 
# encoding of all samples, one per line. This would be the GROUND TRUTH encoding of that partition.

# In this case, we use the samples.test.txt file (so, the test partition)
# and get all its GOLDEN sequences in an LMX file called "groundtruth.testNoStemDir.lmx"

# ALSO create a folder of the images listed in the sample file (in this case, the test set)

from pathlib import Path
import os
import shutil


input_file = Path("../samples.test.txt")
output_file = Path("../ground-truth/groundtruth.fulltokens.test.lmx")

dst_dir = "../ground-truth/samples-test-images"
os.makedirs(dst_dir, exist_ok=True)

with input_file.open("r", encoding="utf-8") as infile, \
	output_file.open("w", encoding="utf-8") as outfile:
	for n, sample in enumerate(infile):
		sample_filepath = "../ground-truth/" + sample.strip() + ".lmx"
		with open(sample_filepath, encoding="utf-8") as samplefile:
			all_tokens = samplefile.readlines()

		result = " ".join(token.strip() for token in all_tokens)
		print(result)

		outfile.write(result + "\n")

		sample_imagepath = "../" + sample.strip() + ".jpg"
		path = Path(sample.strip()+".jpg")
		result = f"{path.parent.name}-{path.name}"
		dst = os.path.join(dst_dir, f"out{n+1}_{result}")
		shutil.copy2(sample_imagepath, dst)
