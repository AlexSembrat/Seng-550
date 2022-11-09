import sys

for line in sys.stdin:
    #remove white spaces and split into individual items
    items = line.strip().split()
    length = len(items)
    #print out items and their pairs
    for i in range(0, length):
        for j in range(0, length):
            if i != j:
                print("{}\t{}\t1".format(items[i], items[j]))
                print("{}\t-\t".format(items[i]))