def isIntegerString(s):
    try:
        i = int(s)
    except ValueError:
        return False
    return True

def flattenListString(lst):
    string = ""
    for line in lst:
        string += line
    return string

def getSyllableDict():
    f = open('data/syllable_dictionary.txt', 'r')
    word_to_syllable = {}
    for line in f:
        line = line.split()
        (word, syllables) = (line[0], line[1:])
        word_to_syllable[word] = syllables
    return word_to_syllable

def getWordNumDict():
    word_to_num = {}
    counter = 0
    word_to_syllable = getSyllableDict()
    for word in word_to_syllable:
        word_to_num[word] = counter
        counter += 1
    return(word_to_num)

def nums_to_words(line):
    word_to_num = getWordNumDict()
    for n in line:
        for k in word_to_num:
            if word_to_num[k] == n:
                print (k)
