import sys

count = 0
total = 0
lastKey1 = None
lastKey2 = None

for line in sys.stdin:
    #strip and split into items
    items = line.strip().split("\t")
   
    #get the 2 items
    key = items[0]
    key2 = items[1]
    #Outer if,elif,else accounts for key 1 pairs
    if lastKey1 is None:
        lastKey1 = key
        lastKey2 = key2
        total = total + 1
    elif lastKey1 == key:
        #Inner if,elif,else accounts for key 1 pairs
        if key2 == "-":
            total = total + 1
        elif lastKey2 == "-":
            lastKey2 = key2
            count = count + 1
        elif lastKey2 == key2:
            count = count + 1
        else:
            print("{} {} {}".format(lastKey1, lastKey2, float(count) / float(total)))
            lastKey2 = key2
            count = 1
    else:
        print("{} {} {}".format(lastKey1, lastKey2, float(count)/float(total)))
        lastKey1 = key
        lastKey2 = key2
        total = 1

#Print the final entry
print("{} {} {}".format(lastKey1, lastKey2, float(count)/float(total)))