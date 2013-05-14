# Rachel Friedman - 5/11/13

import cPickle, random

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    dividers = sorted(random.sample(xrange(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def genLine(syllables, dictList):
    line = ""
    numWords = random.randint(1, syllables-2)  # determines the number of words to be built to fill out the required syllables
    if numWords == 1 and syllables > 5:  # to make sure not too many extremely long words are built
        numWords = random.randint(1, 2)
    syllLst = constrained_sum_sample_pos(numWords, syllables)

    for syllable in syllLst: # 1 and 3 chance for the syllable to be built from each of the dictionaries
        chance = random.randint(1, 3)
        if syllable > 1 and chance == 2:
            bgram = random.choice(dictList[1][syllable])
            line += bgram[0] + ' ' + bgram[1] + ' '
        elif syllable > 1 and chance == 3:
            bgram = random.choice(dictList[2][syllable])
            line += bgram[0] + ' ' + bgram[1] + ' '
        else:
            line += random.choice(dictList[0][syllable]) + ' ' # always built from normal syllable dictionary if we need a 1 syllable word (no 1 syllable bigrams)
    return line + '\n'

def genHaiku(dictList):
    haiku = ""
    for num in [5, 7, 5]:
        haiku += genLine(num, dictList)
    return haiku + "\n"

def main():
    file = open("syllableDict.txt", "rb")
    dict = cPickle.load(file) # loads the already created syllable dictionary consisting of 50,000+ words
    brownBDict = cPickle.load(open("brownBigramDict.txt", "rb"))  # dictionary consisting of bigrams from the brown corpus
    gutenBDict = cPickle.load(open("gutenbergBigramDict.txt", "rb")) # dictionary consisting of bigrams from the gutenberg corpus
    dictList = [dict, brownBDict, gutenBDict] # list of all the dictionaries
    outFile = open("randomHaiku.txt", "w")

    for _ in range(int(raw_input("How many Haiku? "))):
        outFile.write(genHaiku(dictList)) # writes haiku to randomHaiku.txt file

main()
