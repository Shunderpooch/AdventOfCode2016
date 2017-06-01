"""
Arthur Dooner
Advent of Code Day 3
Challenge 2
"""

import sys
TOTAL_VALID_TRIANGLES = 0

with open("triangles.txt", "r") as filestream:
    LINE_LIST = []
    for line in filestream:
        TEMP_LINE_INPUT = [int(s) for s in line.split() if s.isdigit()]
        #print(TEMP_LINE_INPUT)
        TEMP_LINE_INPUT = list(map(int, TEMP_LINE_INPUT))
        LINE_LIST.append(TEMP_LINE_INPUT)
        #print(LINE_LIST)
        if (len(LINE_LIST) == 3):
            for i in range(0, 3):
                if LINE_LIST[0][i] + LINE_LIST[1][i] > LINE_LIST[2][i] and LINE_LIST[0][i] + LINE_LIST[2][i] > LINE_LIST[1][i] and LINE_LIST[1][i] + LINE_LIST[2][i] > LINE_LIST[0][i]:
                    TOTAL_VALID_TRIANGLES += 1
            LINE_LIST = []

    print("The total valid triangles are: " + str(TOTAL_VALID_TRIANGLES))

sys.stdout.flush()