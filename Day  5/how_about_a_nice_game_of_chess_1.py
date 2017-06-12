"""
Arthur Dooner
Advent of Code Day 5
Challenge 1
"""

import sys
import hashlib

def md5_func(string):
    md5result = hashlib.md5()
    md5result.update(string.encode('utf-8'))
    return md5result.hexdigest()

INTEGER_ID = 0
PASSWORD = ""

if len(sys.argv) < 2:
    print("Please pass the puzzle input as a command line argument.")
    exit(0)

while len(PASSWORD) < 8:
    temp_md5 = md5_func(sys.argv[1] + str(INTEGER_ID))
    if temp_md5[:5] == "00000":
        print(INTEGER_ID)
        PASSWORD += temp_md5[5]
    INTEGER_ID += 1

print("The password for the door is:" + PASSWORD)
sys.stdout.flush()