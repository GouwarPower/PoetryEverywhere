# PoetryEverywhere

## Overview
This was originally done as a final project for Grinnell's ENG-295:Lighting The Page. The goal of this project was to reveal poetic form and meter in ostensibly non-poetic writing. It combines course topics of creating new art through erasure and the computational processing of syllabic and metric content

## Package requirements
This project requires the external packages `syllables` and `poetrytools`. `syllables` can be installed from PyPI, but `poetrytools` must be installed from the [source](https://github.com/hyperreality/Poetry-Tools). I have included a makefile to automate the installation of any packages. Simply running `make` will download and install all necessary packages using `pip`.

## Running the program
Running the program is as simple as running the command `python poetry_everywhere.py` and following the command prompts for a choice of a valid text file and action.

### Haikus
Generates haikus drawn from consecutive lines of the text.

### Iambic Pentameter and Trochaic
Finds all of the lines of iambic pentameter or trochaic tetrameter in the text.

### Make Your Own Meter
You choose a base meter, with 0 representing an unstressed syllable and 1 representing a stressed syllable, and the number of occurrences of that meter that you would like
to look for in a line. For example, iambic pentameter would have a base meter of "01" with 5 occurrences to a line.

## Acknowledgments
I would like to thank Professor Eric Simpson for allowing to create this for my final project and giving me the knowledge necessary to make it during ENG-295.  
