from helperFunctions import isIntegerString, getWordNumDict
data = []
#punctuation = [',', ':', ';', '.', '?', '!', '\'']
punctuation = [',', ':', ';', '.', '?', '!']
with open('data/haikus.txt') as f:
    poem = []
    for line in f:
        for punc in punctuation: # Delete punctuation
            line = line.replace(punc, "")

        if not isIntegerString(line):
            poem.append(line)
        elif len(poem) == 0: continue
        else:
            poem = poem[:-1] # Get rid of last newline
            poem[len(poem) - 1] = poem[len(poem) - 1].strip() # Get rid of newline at end of poem
            data.append(poem[:])
            poem = []

    textfile = ""
    # Clean up the data
    for poem in data:
        for line in poem:
            words = line.lower().split()  # Convert each line into a list of words
            if "" in words: words.remove("") # Remove empty strings where punctuation used to be
            for w in words:
                textfile += w + " "

g = open("data/cleanHaikus.txt", "w+")
g.write(textfile)
