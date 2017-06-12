"""
Arthur Dooner
Advent of Code Day 2
Challenge 1
"""

import sys
import unittest

def build_keypad(length, width):
    total_keypad = []
    keypad_counter = 1
    for i in range(0, length): # This is how tall it is (|)
        keypad_line = []
        for j in range (0, width): # This is how wide it is (--)
            keypad_line.append(keypad_counter + j)
        keypad_counter += width
        total_keypad.append(keypad_line)
    return total_keypad

def get_array_loc_of_element(element, length, width):
    length_loc = -1
    width_loc = -1
    if element < 1:
        return (-1, -1)
    for i in range(0, length):
        if element <= (width * (i + 1)): #in this range, since in order keypad
            length_loc = i
            width_loc = element - 1 - (width * i)
            return (length_loc, width_loc)
    return (length_loc, width_loc)

def attempt_move(total_keypad, array_loc, command_params):
    if command_params == (-1, 0) and array_loc[0] == 0:
        return
    elif command_params == (0, 1) and array_loc[1] == (len(total_keypad[0]) - 1):
        return
    elif command_params == (1, 0) and array_loc[0] == (len(total_keypad) - 1):
        return
    elif command_params == (0, -1) and array_loc[1] == 0:
        return
    array_loc[0] += command_params[0]
    array_loc[1] += command_params[1]

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(get_array_loc_of_element(5, 3, 3), (1, 1))
        self.assertEqual(get_array_loc_of_element(6, 3, 3), (1, 2))
        self.assertEqual(get_array_loc_of_element(10, 3, 3), (-1, -1))
        self.assertEqual(get_array_loc_of_element(10, 3, 3), (-1, -1))

#unittest.main()
total_keypad = build_keypad(3, 3)
array_loc = get_array_loc_of_element(5, 3, 3)
array_loc_as_list = [array_loc[0], array_loc[1]]
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