from helperFunctions import isIntegerString, getWordNumDict
data = []
#punctuation = [',', ':', ';', '.', '?', '!', '\'']
punctuation = [',', ':', ';', '.', '?', '!']
with open('data/shakespeare.txt') as f:
    poem = []
    for line in f:
        for punc in punctuation: # Delete punctuation
            line = line.replace(punc, "")

        if not isIntegerString(line):
            poem.append(line)
        elif len(poem) == 0: continue
        else:
            poem = poem[:-2] # Get rid of last two newlines
            poem[len(poem) - 1] = poem[len(poem) - 1].strip() # Get rid of newline at end of poem
            data.append(poem[:])
            poem = []

    word_to_num = getWordNumDict()
    textfile = ""
    # Clean up the data
    for poem in data:
        for line in poem:
            words = line.lower().split()  # Convert each line into a list of words
            if "" in words: words.remove("") # Remove empty strings where punctuation used to be
            if all(map(lambda w: w in word_to_num.keys(), words)): # Only consider lines that have all words in our dictionary
                for w in words:
                    textfile += w + " "

g = open("data/cleanShakespeare.txt", "w+")
g.write(textfile)
