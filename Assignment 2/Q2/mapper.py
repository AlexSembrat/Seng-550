import sys

for line in sys.stdin:
    #strip
    lineArray = line.strip().split()
    #get key and values
    key = lineArray[0]
	
    values = lineArray[1].split("|")
    adjacentNodes = values[0]
    score = values[1]
    color = values[2]
    parent = values[3]

    #identify and change grey nodes
    if color == "GRAY":
        print("{}\t{}|{}|{}|{}".format(key, adjacentNodes, score, "BLACK", parent))
        childsScore = str(int(score) + 1)
        for child in adjacentNodes.split(","):
            print("{}\t{}|{}|{}|{}".format(child, "null", childsScore, "GRAY", key))
    #print the white and black nodes
    else:
        print("{}\t{}|{}|{}|{}".format(key, adjacentNodes, score, color, parent))