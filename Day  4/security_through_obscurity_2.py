"""
Arthur Dooner
Advent of Code Day 4
Challenge 2
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
    TARGET_FILE = open("roomnames.txt", 'w')
    SAVED_SECTOR_ID = 0
    for line in filestream:
        TEMP_LINE_INPUT = line.split('-') #split everything by the '-' delim to get each word
        last_piece = TEMP_LINE_INPUT.pop() #pop off the last piece (the sectorID and checksum)
        # Merge the array into one character set
        generated_checksum = generate_checksum(TEMP_LINE_INPUT)
        # Gather the actual checksum and compare it with the generated checksum
        last_piece_list = last_piece.split('[')
        amount_to_increment = int(last_piece_list[0])
        if generated_checksum == (last_piece_list[1][:5]):
            new_input = []
            for word in TEMP_LINE_INPUT:
                new_word = ""
                for character in word:
                    temp_char = chr(ord(character) + (amount_to_increment % 26))
                    new_word += temp_char if ord(temp_char) < 123 else chr(ord(temp_char) - 26)
                new_input.append(new_word)
            temp_sentence = " ".join(new_input)
            if temp_sentence.count("northpole object storage") > 0:
                SAVED_SECTOR_ID = amount_to_increment
            TARGET_FILE.write(temp_sentence + "\n")
    print("The SectorID of 'northpole object storage' is: " + str(SAVED_SECTOR_ID))

sys.stdout.flush()