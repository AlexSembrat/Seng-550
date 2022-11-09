import sys
import re

for line in sys.stdin:
    #remove white spaces from start and end
    line = line.strip()
    
    #set all to lowercase
    line = line.lower()
    
    #remove all punctuation using regex
    line = re.sub(r'[^\w\s]','', line)

   #split the line into individual words
    wordArray = line.split()

    for word in wordArray:
        firstLetter = str(word[0])
        if firstLetter.isdigit():
            key = "42"
        else:
            key = firstLetter
        print("{}\t{}\t{}".format(key, word, ""))