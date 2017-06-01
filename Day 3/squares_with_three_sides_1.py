"""
Arthur Dooner
Advent of Code Day 3
Challenge 1
"""

import sys
TOTAL_VALID_TRIANGLES = 0

with open("triangles.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = [int(s) for s in line.split() if s.isdigit()]
        print(TEMP_LINE_INPUT)
        TEMP_LINE_INPUT = list(map(int, TEMP_LINE_INPUT))
        TEMP_LINE_INPUT.sort()
        if TEMP_LINE_INPUT[0] + TEMP_LINE_INPUT[1] > TEMP_LINE_INPUT[2]:
            TOTAL_VALID_TRIANGLES += 1

    print("The total valid triangles are: " + str(TOTAL_VALID_TRIANGLES))

sys.stdout.flush()