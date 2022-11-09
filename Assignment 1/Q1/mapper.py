import sys
import random

for line in sys.stdin:
    line = line.strip()
    randNum = random.randint(1, 10)
    if randNum == 5:
        print("{} {}".format(line,""))