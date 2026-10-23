# README
This directory contains the OMR data for the manuscript _GCA-Gaha 1_ to be used with [zeus](https://github.com/OmniOMR/zeus/). The data consists of two types of files (image and sequence encoding) for each of the staff region in the 27 pieces of this music book (see [samples folder](./samples)):
- The **staff region image as JPEG**
- The **sequence of music symbols** of each of these staff regions. The encoding chosen for these sequences is _\*\*mens_. Some points:
  - The beams, which are not that common in mensural notation, are currently encoded using the characters `(` and `)` to indicate the start and the end of a beam (these are not part of _\*\*mens_ and we decided to not go for their usual encoding in _\*\*kern_ as it implies the use of `L` and `J`, and `L` is reserved for longas in  _\*\*mens_).

  The files have the **extension `.lmx`** to work with the Zeus pickling functionality, but it is important to know that **the format is not LMX, but _\*\*mens_ (as indicated before)**.
