import sys

lastWord = None
fileNames = []
for line in sys.stdin:
    #remove spaces
    line = line.strip()
    #split into the word and fileName
    word, fileName = line.split()

    if lastWord is None:
        lastWord = word
        fileNames.append(fileName)
    elif lastWord == word:
        if fileName not in fileNames:
            fileNames.append(fileName)
    else:
        #print the word and its fileNames
        print(lastWord,"  ",fileNames)
        #next word
        lastWord = word
        fileNames = [fileName]

#print the final word
if lastWord is not None:
    print(lastWord,"  ",fileNames)