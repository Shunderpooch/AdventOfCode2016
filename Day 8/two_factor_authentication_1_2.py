"""
Arthur Dooner
Advent of Code Day 8
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

def print_display(board_input):
    for board_row in board_input:
        printable_string = ""
        for element in board_row:
            if element is False:
                printable_string += " "
            else:
                printable_string += "#"
        print(printable_string)

def rectangle_func(board_input, width, height):
    if len(board_input[0]) < width or len(board_input) < height:
        raise IndexError("Rectangle larger than size of board")
    else:
        for height_index in range(0, height):
            for width_index in range(0, width):
                board_input[height_index][width_index] = True

def rotate_column(board_input, column, amount):
    if len(board_input[0]) - 1 < column:
        raise IndexError("Column specified is out of range of board")
    else:
        amount_to_move = amount % len(board_input)
        list_of_elements = []
        for index in range(0, len(board_input)):
            list_of_elements.append(board_input[index][column])
        for index in range(0, len(board_input)):
            board_input[(index + amount_to_move) % len(board_input)][column] = list_of_elements[index]

def rotate_row(board_input, row, amount):
    if len(board_input) - 1 < row:
        raise IndexError("Row specified is out of range of board")
    else:
        amount_to_move = amount % len(board_input[0])
        list_of_elements = []
        for index in range(0, len(board_input[0])):
            list_of_elements.append(board_input[row][index])
        for index in range(0, len(board_input[0])):
            board_input[row][(index + amount_to_move) % len(board_input[0])] = list_of_elements[index]

TOTAL_ON = 0
WIDTH = 0
HEIGHT = 0
if len(sys.argv) != 3:
    raise Exception("Invalid number of arguments")
try:
    WIDTH = int(sys.argv[1])
    HEIGHT = int(sys.argv[2])
except ValueError:
    exit(1)

BOARD_INPUT = []
for index in range(0, HEIGHT):
    temp_list = [False] * WIDTH
    BOARD_INPUT.append(temp_list)

with open("state_shifts.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = line.rstrip()
        if "rect" in TEMP_LINE_INPUT:
            TEMP_LINE_INPUT = re.split(' |x', TEMP_LINE_INPUT)
            # index 1 is width, 2 is height in TEMP_LINE_INPUT list
            rectangle_func(BOARD_INPUT, int(TEMP_LINE_INPUT[1]), int(TEMP_LINE_INPUT[2]))
        elif "rotate column" in TEMP_LINE_INPUT:
            TEMP_LINE_INPUT = re.split(' |=', TEMP_LINE_INPUT)
            rotate_column(BOARD_INPUT, int(TEMP_LINE_INPUT[3]), int(TEMP_LINE_INPUT[5]))
            # index 3 is column, 5 is amount
        elif "rotate row" in TEMP_LINE_INPUT:
            TEMP_LINE_INPUT = re.split(' |=', TEMP_LINE_INPUT)
            rotate_row(BOARD_INPUT, int(TEMP_LINE_INPUT[3]), int(TEMP_LINE_INPUT[5]))
            # index 3 is row, 5 is amount
        #TEMP_LINE_INPUT = re.split('\[|\]', TEMP_LINE_INPUT)

for index in range(0, HEIGHT):
    for index1 in range(0, WIDTH):
        if BOARD_INPUT[index][index1] is True:
            TOTAL_ON += 1
print("The total number of pixels on on the small display is: " + str(TOTAL_ON))

"""
Arthur Dooner
Advent of Code Day 8
Challenge 2
"""
print("The code is displayed below on that display:")
print_display(BOARD_INPUT)

sys.stdout.flush()