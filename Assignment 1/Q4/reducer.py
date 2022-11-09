import sys

lastWord = None
for line in sys.stdin:
    line = line.strip()
    key, word = line.split()

    if lastWord is None:
        lastWord = word
    elif lastWord == word:
        continue
    else:
        print("{}\t{}".format(lastWord, ""))

        #Next
        lastWord = word

#print final word
if lastWord is not None:
    print("{}\t{}".format(lastWord, ""))