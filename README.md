# README
This directory contains the OMR data for the manuscript _GCA-Gaha 1_ to be used with [zeus](https://github.com/OmniOMR/zeus/). The data consists of two types of files (image and sequence encoding) for each of the staff region in the 27 pieces of this music book (see [samples folder](./samples)):
- The **staff region image as JPEG**
- The **sequence of music symbols** of each of these staff regions. The encoding chosen for these sequences is a subtokenization of _\*\*smens_ or _semantic mens_. Some points:
  - _Semantic mens_ is a variation of _\*\*mens_, the Humdrum encoding for mensural notation. (Main difference: dots are encoded with `.`, as in _\*\*kern_, instead of `:`, as should be done in _\*\*mens_; it also includes characters for beams that come from _\*\*kern_, the `L` and `J` for starting and ending beam which are not part of _\*\*mens_.)
  - The _semantic mens_ has been sub-tokenised to separate the different type of information of a \*\*smens token (e.g., `[s~g#` is subtokenized into `[ s ~ g#`, to account for the `[` ligature start, the semibrevis note shape `s`, the coloration of the note `~`, and its pitch `g#`) reducing the vocabulary that the OMR model needs to deal with.

  The files have the **extension `.lmx`** to work with the Zeus pickling functionality, but it is important to know that **the format is not LMX, but a subtokenization of _\*\*smens_ (as indicated before)**.
