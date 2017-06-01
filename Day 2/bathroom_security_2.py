"""
Arthur Dooner
Advent of Code Day 2
Challenge 2
"""

import sys
import unittest

def attempt_move(total_keypad, array_loc, command_params):
    if command_params == (-1, 0) and array_loc[0] == 0 or command_params == (-1, 0) and total_keypad[array_loc[0] - 1][array_loc[1]] == "0":
        return
    elif command_params == (0, 1) and array_loc[1] == (len(total_keypad[0]) - 1) or command_params == (0, 1) and total_keypad[array_loc[0]][array_loc[1] + 1] == "0":
        return
    elif command_params == (1, 0) and array_loc[0] == (len(total_keypad) - 1) or command_params == (1, 0) and total_keypad[array_loc[0] + 1][array_loc[1]] == "0":
        return
    elif command_params == (0, -1) and array_loc[1] == 0 or command_params == (0, -1) and total_keypad[array_loc[0]][array_loc[1] - 1] == "0":
        return
    array_loc[0] += command_params[0]
    array_loc[1] += command_params[1]

#unittest.main()
total_keypad = [["0", "0", "1", "0", "0"], ["0", "2", "3", "4", "0"], ["5", "6", "7", "8", "9"], ["0", "A", "B", "C", "0"], ["0", "0", "D", "0", "0"]]
array_loc = (2, 0)
array_loc_as_list = [array_loc[0], array_loc[1]]
print(total_keypad[2][0])
code = []
with open("bathroom_code.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = list(line)
        #print(TEMP_LINE_INPUT)
        while TEMP_LINE_INPUT: # Implicit boolean in the list having elements
            command = TEMP_LINE_INPUT.pop(0)
            command_params = (-1, -1)
            if command == 'U':
                command_params = (-1, 0) 
            elif command == 'R':
                command_params = (0, 1)
            elif command == 'D':
                command_params = (1, 0)
            elif command == 'L':
                command_params = (0, -1)
            if command_params != (-1, -1): #something didn't go horribly wrong
                attempt_move(total_keypad, array_loc_as_list, command_params)
        #print(str(total_keypad[array_loc_as_list[0]][array_loc_as_list[1]]))
        code.append(total_keypad[array_loc_as_list[0]][array_loc_as_list[1]])

    print("The code for the bathroom is: " + "".join(map(str, code)))

sys.stdout.flush()