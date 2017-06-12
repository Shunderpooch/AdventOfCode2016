"""
Arthur Dooner
Advent of Code Day 7
Challenge 2
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

def generate_aba_list(input_string):
    temp_list = []
    for index_tracker in range(0, len(input_string) - 2):
        if (input_string[index_tracker] == input_string[index_tracker + 2] and # In ABA, A1 equals A2 check
            input_string[index_tracker] != input_string[index_tracker + 1]): #in ABA, A != B check
            temp_list.append(input_string[index_tracker:(index_tracker + 3)])
    return temp_list


TOTAL_SSL = 0
with open("ipv7_addresses.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = line.rstrip()
        TEMP_LINE_INPUT = re.split('\[|\]', TEMP_LINE_INPUT)
        state_tracker = 0
        result = False
        aba_list = []
        for string in TEMP_LINE_INPUT: #First we have to build the list of potential options
            if state_tracker % 2 == 0: # We want there to be an abba for TLS
                aba_list.extend(generate_aba_list(string))
            state_tracker += 1
        state_tracker = 0
        for string in TEMP_LINE_INPUT:
            if state_tracker % 2 == 1:
                #print(aba_list)
                for aba_selection in aba_list:
                    potential_bab = str(aba_selection[1]) + str(aba_selection[0]) + str(aba_selection[1])
                    if potential_bab in string:
                        result = True
            state_tracker += 1                
        if result:
            TOTAL_SSL += 1
print("The total number of IPs that support SSL of EBHQ's Local Network are: " + str(TOTAL_SSL))
sys.stdout.flush()