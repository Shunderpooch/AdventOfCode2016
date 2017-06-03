"""
Arthur Dooner
Advent of Code Day 6
Challenge 2
"""

import sys

COLUMN_DICT_LIST = []
INIT = True
with open("garbledmessage.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = line.rstrip()
        if INIT:
            for character in TEMP_LINE_INPUT:
                TEMP_DICT = {}
                COLUMN_DICT_LIST.append(TEMP_DICT)
                INIT = False
        temp_counter = 0
        for character in TEMP_LINE_INPUT:
            COLUMN_DICT_LIST[temp_counter][character] = COLUMN_DICT_LIST[temp_counter].get(character, 0) + 1
            temp_counter += 1

STRING_RESULT = ""
for dictionary in COLUMN_DICT_LIST:
    # print(dictionary)
    temp_list = sorted(dictionary, key=dictionary.__getitem__)
    # print(temp_list)
    if temp_list:
        STRING_RESULT += temp_list[0]

print("The message is, accounting this time for the least likely letters in each column: " + STRING_RESULT)
sys.stdout.flush()