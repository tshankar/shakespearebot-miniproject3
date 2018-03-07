import numpy as np
from helperFunctions import isIntegerString

data = []
stripped_data = []
punctuation = [",", ":", ";", ".", "?", "!"]
data = np.loadtxt("data/shakespeare.txt", delimiter='\n', dtype='bytes').astype(str)

# Strip all whitespace (including whitespace on last line of poems)
for i in range(len(data)):
    line = data[i].strip()
    if not isIntegerString(line):
        stripped_data.append(line)

print (stripped_data)
