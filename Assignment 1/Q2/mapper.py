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

    #create a digram if there are 2 or more words on a line
    if len(wordArray) > 1:
        for i in range(0, len(wordArray) - 1):
            firstWord = wordArray[i].strip()
            secondWord = wordArray[i + 1].strip()
            print("{} {} {}".format(firstWord, secondWord, 1))