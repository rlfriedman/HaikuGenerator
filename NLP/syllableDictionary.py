# Rachel Friedman - 5/11/13

import cPickle
from nltk.corpus import wordnet

def genSyllableDict():
    """ Creates a dictionary consisting of number of syllables as keys and lists of words as values"""

    syllables = {}
    nums = [str(x) for x in range(15)]

    for i in range(0, 15):
        syllables[i] = list()

    f = open("cmudict.txt", "r") # CMU dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict
    
    for line in f: 
        count = 0
        line = line.split('  ')
        word = line[0]
        sylLst = line[1]

        for char in sylLst:
            if char in nums:
                count += 1
                
        if word[-1] != ')' and "'" not in word and wordnet.synsets(word): # no apostrophes and makes sure the word isn't a proper name
            syllables[count].append(word.lower()) 

    return syllables

syllableDict = genSyllableDict()
cPickle.dump(syllableDict, open("syllableDict.txt", "wb")) # saves syllable dictionary for later use so we don't have to generate again