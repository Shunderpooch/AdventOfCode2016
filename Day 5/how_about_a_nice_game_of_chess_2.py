"""
Arthur Dooner
Advent of Code Day 5
Challenge 2
"""

import sys
import hashlib

def md5_func(string):
    md5result = hashlib.md5()
    md5result.update(string.encode('utf-8'))
    return md5result.hexdigest()

INTEGER_ID = 0
PASSWORD = ""
DICT_OF_SOLUTIONS = {}

if len(sys.argv) < 2:
    print("Please pass the puzzle input as a command line argument.")
    exit(0)

while len(DICT_OF_SOLUTIONS) < 8:
    temp_md5 = md5_func(sys.argv[1] + str(INTEGER_ID))
    if temp_md5[:5] == "00000":
        print(INTEGER_ID)
        TEMP_POSITION = temp_md5[5]
        if TEMP_POSITION.isdigit() and int(TEMP_POSITION) < 8:
            if int(TEMP_POSITION) not in DICT_OF_SOLUTIONS:
                DICT_OF_SOLUTIONS[int(TEMP_POSITION)] = temp_md5[6]
    INTEGER_ID += 1
PASSWORD = "".join(x[1] for x in sorted(DICT_OF_SOLUTIONS.items()))
print("The password for the door is:" + PASSWORD)
sys.stdout.flush()