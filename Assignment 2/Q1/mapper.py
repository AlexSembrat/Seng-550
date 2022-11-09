import sys

for line in sys.stdin:
    row, col, value = line.strip().split(",")
    print("{},{},{}".format(col, row, value))