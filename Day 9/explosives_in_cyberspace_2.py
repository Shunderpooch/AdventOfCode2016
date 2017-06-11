"""
Arthur Dooner
Advent of Code Day 9
Challenge 2
"""
import sys
import re

def get_decompression_length(full_selection):
    line_index = 0
    selection_len = 0
    while line_index < len(full_selection):
        if full_selection[line_index] == "(":
            length_to_select = 0
            times_to_repeat = 0
            num_counter = 0
            while(full_selection[line_index + num_counter] != "x"): # Get the length that we'll duplicate
                num_counter += 1
            length_to_select = int(full_selection[(line_index + 1):(line_index + num_counter)])
            line_index = line_index + num_counter
            num_counter = 0
            while(full_selection[line_index + num_counter] != ")"): # Get the amount of times we'll duplicate
                num_counter += 1
            times_to_repeat = int(full_selection[(line_index + 1):(line_index + num_counter)])
            line_index = line_index + num_counter + 1 # Set line index to be exactly where we want to start reading
            selection = full_selection[line_index:(line_index + length_to_select)]
            line_index = line_index + length_to_select
            selection_len += get_decompression_length(selection) * times_to_repeat
        else:
            selection_len += 1
            line_index += 1
    return selection_len
    

with open("compressed_file.txt", "r") as filestream:
    LINE_LIST = []
    TARGET_FILE = open("decompressed_file.txt", 'w')
    file_len = 0
    for line in filestream:
        TEMP_LINE_INPUT = line.rstrip()
        file_len = get_decompression_length(TEMP_LINE_INPUT)

    print("The length of the decompressed file using version two of the algorithm is: " + str(file_len))

sys.stdout.flush()