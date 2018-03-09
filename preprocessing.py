import numpy as np
from helperFunctions import isIntegerString, flattenListString, getSyllableDict, getWordNumDict, nums_to_words

''' Returns data = [[line1], [line2],...]'''
def byLine():
    data = []
    stripped_data = []
    #punctuation = [',', ':', ';', '.', '?', '!', '\'']
    punctuation = [',', ':', ';', '.', '?', '!']
    data = np.loadtxt("data/shakespeare.txt", delimiter='\n', dtype='bytes').astype(str)

    # Strip all whitespace (including whitespace on last line of poems)
    for i in range(len(data)):
        line = data[i].strip()
        # for punc in punctuation: # Delete punctuation
        #     line = line.replace(punc, "")

        if not isIntegerString(line):
            stripped_data.append(line)

    return stripped_data

''' Returns data = [[poem1], [poem2],...], where each poem is [[line1], [line2]...] if not flattened.
    If flattened, each poem is [line1line2....]. '''
def byPoem(flatten=False):
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
                if flatten:
                    poem = flattenListString(poem)
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

''' Returns training data for RNN split by sequences of length seqLength'''
def getTrainingDataRNN(seqLength):
    data = byPoem()
    segments = []
    trainingXchars = []
    trainingYchars = []
    trainingXnums = []
    trainingYnums = []

    # Get first seqLength characters, and the next character, of each line
    for poem in data:
        for line in poem:
            if len(line) > seqLength:
                segments.append([line[:seqLength], line[seqLength]])

    # Put the first seqLength characters in trainingXchars and the next character in traininYchars
    for s in range(len(segments)):
        trainingXchars.append(segments[s][0])
        trainingYchars.append(segments[s][1])

    # Convert the characters in X and Y into numbers
    characterMap = 'abcdefghijklmnopqrstuvwxyz-()\' \n'

    for i in range(len(trainingXchars)):
        trainingXnums.append([characterMap.index(j) for j in trainingXchars[i].lower()])
    for i in range(len(trainingYchars)):
        trainingYnums.append([characterMap.index(j) for j in trainingYchars[i].lower()])

    trainingYnums = [y for x in trainingYnums for y in x] # Flatten list

    return (trainingXnums, trainingYnums)

def getTrainingDataHMM(seqLength):
    data = byPoem()
    segments = []
    trainingXwords = []
    trainingYwords = []
    trainingXnums = []
    trainingYnums = []
    word_to_num = getWordNumDict()

    for poem in data:
        for line in poem:
            words = line.lower().split()  # Convert each line into a list of words
            if "" in words: words.remove("") # Remove empty strings where punctuation used to be
            if all(map(lambda w: w in word_to_num.keys(), words)): # Only consider lines that have all words in our dictionary
                i = 0
                while i + seqLength < len(words):
                    segments.append([words[i:i+seqLength], words[i+seqLength]])
                    i += seqLength

    # Put the first seqLength characters in trainingXchars and the next character in traininYchars
    for s in range(len(segments)):
        trainingXwords.append(segments[s][0])
        trainingYwords.append(segments[s][1])

    for seq in trainingXwords:
        nums = list(map(lambda x: word_to_num[x], seq))
        trainingXnums.append(nums)
    for w in trainingYwords:
        trainingYnums.append(word_to_num[w])


    return (trainingXnums, trainingYnums)

#print (getTrainingDataHMM(5))
