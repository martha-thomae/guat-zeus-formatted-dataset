# README
This directory contains the OMR data for the manuscript _GCA-Gaha 1_ to be used with [zeus](https://github.com/OmniOMR/zeus/). The data consists of the following files for each of the 27 pieces in the mansucript:
- The staff regions as JPEG images
- The sequence of music symbols of each of these staff regions. The encoding chosen for these sequences is _\*\*smens_ or _semantic mens_. This is a variation of _\*\*mens_, the Humdrum encoding for mensural notation. (Main difference: dots are encoded with `.`, as in _\*\*kern_, instead of `:`, as should be done in _\*\*mens_). The files have the extension `.lmx` to work with the Zeus pickling functionality, but it is important to know that the format is not LMX, but _\*\*smens_ (as indicated before).
