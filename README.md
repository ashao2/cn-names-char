# cn-names-char
mingzi.py is a Python script that takes a plain text file of Chinese names and returns a results.txt file containing:
- Top n surnames
- Top n characters in given names
- Top n two-character given names
- Top n first characters in two-character given names
- Top n second characters in two-character given names
- Top n single-character given names
- Top n full names
Fewer than n names/characters will be printed once the frequency reaches 1.

To run the script, run python3 mingzi.py <path to input file>.txt <n, number of names/characters to print>. I've provided processed.txt that you can try using. It contains names of popular Chinese female entertainers from various decades.
  
Currently, I only support names with one-character surnames and one-character or two-character given names.
