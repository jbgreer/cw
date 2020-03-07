#!/usr/bin/python3
import sys
from didah import Didah

# map from character to cw
symbol2cw_map = {}

# convert entries of form TEXT: [.-]+ into a map of characters to cw
def buildcwmap(filename):
    with open(filename) as f:
        for line in f:
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            (symbol, cw) = line.strip().replace(' ', '').replace("\t", '').split(':')
            symbol2cw_map[symbol] = cw

def symbol2cw(symbol):
    cw = symbol2cw_map.get(symbol)
    if cw == None:
        cw = "Unknown"
    return cw

def cw2sound(didah, cw_words):
    for word in cw_words:
        print("word>" + " ".join(word) + "<")
        for letter in word:
            print("letter>" + letter + "<")
            for symbol in letter:
                if symbol == '.':
                    didah.dit()
                    didah.space()
                elif symbol == '-':
                    didah.dah()
                    didah.space()
                else:
                    pass
            didah.letter_space()
        didah.word_space()



def main(inputfile):
    didah = Didah()
    for line in f:
        print(line)
        words = line.strip().upper().split(' ')
        cw_words = []
        for word in words:
            cw_word = []
            for symbol in word:
                cw = symbol2cw(symbol)
                cw_word.append(cw)
            print(cw_word)
            cw_words.append(cw_word)
        cw2sound(didah, cw_words)

if __name__ == "__main__":
    nargs = len(sys.argv)

    if nargs < 2:
        print("usage: " + sys.argv[0] + " <dictionary>> [inputfile]")
        sys.exit(1)

    buildcwmap(sys.argv[1])

    if nargs == 3:
        f = open(sys.argv[2], "r") 
    else:
        f = sys.stdin

    main(f)

