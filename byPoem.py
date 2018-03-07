import numpy as np
from helperFunctions import isIntegerString

data = []
stripped_data = []
punctuation = [",", ":", ";", ".", "?", "!"]
with open('data/shakespeare.txt') as f:
    poem = []
    for line in f:
        if not isIntegerString(line):
            poem.append(line)
        elif len(poem) == 0: continue
        else:
            poem = poem[:-2] # Get rid of last two newlines
            poem[len(poem) - 1] = poem[len(poem) - 1].strip() # Get rid of newline at end of poem
            data.append(poem[:])
            poem = []

print (data)
