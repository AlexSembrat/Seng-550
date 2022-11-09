import sys
import re
import os

for line in sys.stdin:
    #remove white spaces from start and end
    line = line.strip()
    
    #set all to lowercase
    line = line.lower()
    
    #remove all punctuation using regex
    line = re.sub(r'[^\w\s]','', line)

   #split the line into individual words
    wordArray = line.split()

    #Find file name
    filePath = os.environ['mapreduce_map_input_file']
    filePath = filePath.split("/")
    fileName = filePath[-1]
    #print the word and the fileName
    for word in wordArray:
        print("{} {}".format(word, fileName))