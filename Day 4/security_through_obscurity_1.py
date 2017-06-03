"""
Arthur Dooner
Advent of Code Day 4
Challenge 1
"""

import sys
SUM_SECTOR_IDS = 0

def generate_checksum(word_array):
    combined_array = ''.join(word_array)
    letter_count = dict((letter, combined_array.count(letter)) for letter in set(combined_array))
    #this is now a list, alphabetically, of tuples
    sorted_letter_count = sorted(letter_count.items())
    #Now by greatest count with ties decided by alphabetical
    sorted_letter_count.sort(key=lambda x: x[1], reverse=True)
    checksum = ""
    counter = 0
    for y in sorted_letter_count[:5]: #only want the first 5 letters
        checksum += y[0]
    return checksum

with open("realfakerooms.txt", "r") as filestream:
    LINE_LIST = []
    for line in filestream:
        TEMP_LINE_INPUT = line.split('-') #split everything by the '-' delim to get each word
        last_piece = TEMP_LINE_INPUT.pop() #pop off the last piece (the sectorID and checksum)
        # Merge the array into one character set
        generated_checksum = generate_checksum(TEMP_LINE_INPUT)
        # Gather the actual checksum and compare it with the generated checksum
        last_piece_list = last_piece.split('[')
        if generated_checksum == (last_piece_list[1][:5]):
            SUM_SECTOR_IDS += int(last_piece_list[0])
    print("The Sum of Valid SectorIDs are: " + str(SUM_SECTOR_IDS))

sys.stdout.flush()