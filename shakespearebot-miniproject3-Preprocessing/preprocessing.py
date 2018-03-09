import numpy as np
from helperFunctions import isIntegerString, flattenList

''' Returns data = [[line1], [line2],...]'''
def byLine():
    data = []
    stripped_data = []
    punctuation = [",", ":", ";", ".", "?", "!"]
    data = np.loadtxt("data/shakespeare.txt", delimiter='\n', dtype='bytes').astype(str)

    # Strip all whitespace (including whitespace on last line of poems)
    for i in range(len(data)):
        line = data[i].strip()
        if not isIntegerString(line):
            stripped_data.append(line)

    return stripped_data

''' Returns data = [[poem1], [poem2],...], where each poem is [[line1], [line2]...] if not flattened.
    If flattened, each poem is [line1line2....]. '''
def byPoem(flatten=False):
    data = []
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
                if flatten:
                    poem = flattenList(poem)
                data.append(poem[:])
                poem = []
    return data

''' Returns data = [[stanza1], [stanza2]...] '''
def byStanza():
    data = byPoem()
    stanzaData = []
    for poem in data:
        stanzaData.append(poem[:4])
        stanzaData.append(poem[4:8])
        stanzaData.append(poem[8:12])
        stanzaData.append(poem[12:])
    return stanzaData
