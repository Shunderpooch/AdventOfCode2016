"""
Arthur Dooner
Advent of Code Day 9
Challenge 1
"""
import sys
import re

with open("compressed_file.txt", "r") as filestream:
    LINE_LIST = []
    TARGET_FILE = open("decompressed_file.txt", 'w')
    file_len = 0
    for line in filestream:
        TEMP_LINE_INPUT = line.rstrip()
        line_index = 0
        while line_index < len(TEMP_LINE_INPUT):
            if TEMP_LINE_INPUT[line_index] == "(":
                length_to_select = 0
                times_to_repeat = 0
                num_counter = 0
                while(TEMP_LINE_INPUT[line_index + num_counter] != "x"): # Get the length that we'll duplicate
                    num_counter += 1
                length_to_select = int(TEMP_LINE_INPUT[(line_index + 1):(line_index + num_counter)])
                line_index = line_index + num_counter
                num_counter = 0
                while(TEMP_LINE_INPUT[line_index + num_counter] != ")"): # Get the amount of times we'll duplicate
                    num_counter += 1
                times_to_repeat = int(TEMP_LINE_INPUT[(line_index + 1):(line_index + num_counter)])
                line_index = line_index + num_counter + 1 # Set line index to be exactly where we want to start reading
                selection = TEMP_LINE_INPUT[line_index:(line_index + length_to_select)]
                line_index = line_index + length_to_select
                for counter in range(0, times_to_repeat):
                    TARGET_FILE.write(selection)
                    file_len += length_to_select
            else:
                TARGET_FILE.write(TEMP_LINE_INPUT[line_index])
                file_len += 1
                line_index += 1

    print("The length of the decompressed file is:" + str(file_len))

sys.stdout.flush()