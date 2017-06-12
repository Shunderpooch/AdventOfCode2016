"""
Arthur Dooner
Advent of Code Day 7
Challenge 1
"""
import sys
import re

def contains_abba(input_string):
    for index_tracker in range(0, len(input_string) - 3):
        if (input_string[index_tracker + 1] == input_string[index_tracker + 2] and # In ABBA, B1 equals B2 check
                input_string[index_tracker] == input_string[index_tracker + 3] and # In ABBA, A1 equals A2 check
                input_string[index_tracker] != input_string[index_tracker + 1]): # In ABBA, A != B1 check
            return True
    return False

TOTAL_TLS = 0
with open("ipv7_addresses.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = line.rstrip()
        TEMP_LINE_INPUT = re.split('\[|\]', TEMP_LINE_INPUT)
        state_tracker = 0
        positive_example = False
        negative_example = False
        for string in TEMP_LINE_INPUT:
            if state_tracker % 2 == 0: # We want there to be an abba for TLS
                positive_example = positive_example or contains_abba(string)
            elif state_tracker % 2 == 1: # We want there to be no abba for TLS
                negative_example = negative_example or contains_abba(string)
                if negative_example:
                    break
            state_tracker += 1
        if positive_example and not negative_example:
            TOTAL_TLS += 1
print("The total number of IPs that support TLS of EBHQ's Local Network are: " + str(TOTAL_TLS))
sys.stdout.flush()