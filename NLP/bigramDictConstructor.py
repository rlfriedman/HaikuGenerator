# Rachel Friedman - 5/11/13

import nltk.corpus
import nltk.collocations
import collections
import cPickle
from collections import defaultdict

def bigramFinder():
    """Returns a list of popular bigrams from a corpus"""

    bgm = nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(nltk.corpus.gutenberg.words())
    bigramLst = []
    finder.apply_freq_filter(3) # must be found at least 3 times
    bigrams = finder.nbest(bgm.pmi, 10000)
    for i in range(len(bigrams)):
        valid = True
        for j in range(2):
            if bigrams[i][j] in [",", ".", "!", '"']: # must not contain punctuation
                valid = False
        if valid:
            bigramLst.append(bigrams[i])

    return bigramLst

def bigramDict(dictionary, bigramLst):
    """Assigns bigram pairs to correct syllable count in a dictionary"""

    bDict = defaultdict(list)
    for i in range(len(bigramLst)):
        syllSum = 0
        bgm = []
        for j in range(2):
            key = [key for key,value in dictionary.items() if bigramLst[i][j].lower() in value] # finds each word in the bigram in the already created syllable dict
            if key != []:
                syllSum += key[0] # if found, adds the correct number of syllables to the syllable sum for that bigram
                bgm.append(str(bigramLst[i][j]).lower()) # appends that part of the bigram to a list for that bigram
        if len(bgm) == 2 and syllSum <= 7: # if the bigram is full (meaning that both parts passed through the syllable check) adds the list to the list in the bigram dictionary
            bDict[syllSum].append(bgm)
    return bDict

file = open("syllables.txt", "rb")
dict = cPickle.load(file) # loads the already created syllable dictionary

bDict = bigramDict(dict, bigramFinder())
cPickle.dump(bDict, open("gutenbergBigramDict.txt", "wb")) # saves the bigram dictionary to a text file for later use