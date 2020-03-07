#!/usr/bin/python3
import sys
import didah

# map from cw string to letter
cw2textmap = {}

# convert entries of form TEXT: [.-]+ into a map of morse to symbols
def buildcwmap(filename):
    with open(filename) as f:
        for line in f:
            if len(line) == 0:
                continue
            if line[0] == '#':
                continue
            (txt, cw) = line.strip().replace(' ', '').replace("\t", '').split(':')
            cw2textmap[cw] = txt

def cw2text(cw):
    txt = cw2textmap.get(cw)
    if txt == None:
        txt = "Unknown"
    return txt

def main(inputfile):
    for cwline in f:
        #print(cwline)
        cwwords = cwline.strip().split(' ')
        text_words = []
        for cww in cwwords:
            txt = cw2text(cww)
            text_words.append(txt)
        print(cwline + str(text_words))

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

