import sys

lastNode = None
lastAdjNodes = None
lastScore = None
lastColor = None
lastParent = None
for line in sys.stdin:
    
    #get key and values
    lineArray = line.strip().split()
    key = lineArray[0]
    values = lineArray[1].split("|")
    adjacentNodes = values[0]
    score = values[1]
    colour = values[2]
    parent = values[3]

    if lastNode is None:
        lastNode = key
        if adjacentNodes != "null":
            lastAdjNodes = adjacentNodes
        lastScore = score
        lastColor = colour
        lastParent = parent
    #get the correct values for the node    
    elif lastNode == key:
        if adjacentNodes != "null":
            lastAdjNodes = adjacentNodes
        
        if score < lastScore:
            lastScore = score
            lastParent = parent

        if lastColor == "BLACK" or colour == "BLACK":
            lastColor = "BLACK"
        elif lastColor == "WHITE" and colour == "GRAY":
            lastColor = "GRAY"
        elif lastColor == "GRAY" and colour == "GRAY":
            lastColor = "GRAY"
        elif lastColor == "GRAY" and colour == "WHITE":
            lastColor = "GRAY"
    else:
        print("{}\t{}|{}|{}|{}".format(lastNode, lastAdjNodes, lastScore, lastColor, lastParent))
        lastNode = key
        lastAdjNodes = adjacentNodes
        lastScore = score
        lastColor = colour
        lastParent = parent
print("{}\t{}|{}|{}|{}".format(lastNode, lastAdjNodes, lastScore, lastColor, lastParent))