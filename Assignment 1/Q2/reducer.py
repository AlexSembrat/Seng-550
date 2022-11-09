import sys


total = 0
lastDigram = None

for line in sys.stdin:
    #Strip White Spaces
    line = line.strip()
    
    #Seperate into the digram and its count
    digram, count = line.rsplit(' ',1)

    if lastDigram is None:
        lastDigram = digram
        total = int(count)
    if lastDigram == digram:
        total += int(count)
    else:
        print("{}   {}".format(lastDigram, total))
        lastDigram = digram
        total= int(count)

#Print the final digram and its total
if lastDigram is not None:
    print("{}   {}".format(lastDigram, total))