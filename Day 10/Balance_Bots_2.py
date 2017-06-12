"""
Arthur Dooner
Advent of Code Day 10
Challenge 2
"""
import sys
import re


tempfile = open("bot_behavior_2.txt", 'w')

class output:
    output_id = -1
    def __init__(self, output_id):
        self.output_id = output_id
        self.chips = []
    def add_chip(self, chip):
        self.chips.append(chip)
    def log_state(self):
        global tempfile
        if self.chips:
            tempfile.write("Output " + str(self.output_id) + " has chips " + str(self.chips) + ".\n")
class bot:
    bot_id = -1
    bot_give_low = -1
    bot_give_high = -1
    give_output_low = False
    give_output_high = False
    def __init__(self, bot_id, chip=-1, give_low=-1, give_high=-1, give_output_low=False, give_output_high=False):
        self.bot_id = bot_id
        self.chips = []
        if chip != -1:
            self.add_chip(chip, None)
        self.bot_give_low = give_low
        self.bot_give_high = give_high
        self.give_output_low = give_output_low
        self.give_output_high = give_output_high
    def add_chip(self, chip, a_bot_playground):
        if len(self.chips) == 2:
            self.give_chips(a_bot_playground)
        self.chips.append(chip)
        global tempfile
        tempfile.write("Added " + str(chip) + " to " + str(self.bot_id) + "\n")
    def add_instructions(self, give_low, give_high, give_output_low=False, give_output_high=False):
        self.bot_give_low = give_low
        self.bot_give_high = give_high
        self.give_output_low = give_output_low
        self.give_output_high = give_output_high
    def give_chips(self, a_bot_playground):
        if len(self.chips) == 2 and self.bot_give_low != -1 and self.bot_give_high != -1:
            self.chips.sort()
            global tempfile
            tempfile.write("Bot " + str(self.bot_id) + " made the comparison of chips " + str(self.chips[0]) + " and " + str(self.chips[1]) + "!\n")
            if (self.chips[0] == 17 and self.chips[1] == 61):
                print("Bot " + str(self.bot_id) + " made the comparison needed!")
                #exit(0)
            if self.give_output_low:
                tempfile.write("Sending " + str(self.chips[0]) + " to Output " + str(self.bot_give_low) + ".\n")
                a_bot_playground.add_output(self.bot_give_low, self.chips.pop(0))
            else:
                tempfile.write("Sending " + str(self.chips[0]) + " to Bot " + str(self.bot_give_low) + ".\n")
                a_bot_playground.add_bot(self.bot_give_low, self.chips.pop(0))
                # index_to_point = a_bot_playground.get_index_of_bot(self.bot_give_low)
                # a_bot_playground.bot_list[index_to_point].give_chips(a_bot_playground)
            if self.give_output_high:
                tempfile.write("Sending " + str(self.chips[0]) + " to Output " + str(self.bot_give_high) + ".\n")
                a_bot_playground.add_output(self.bot_give_high, self.chips.pop(0))
            else:
                tempfile.write("Sending " + str(self.chips[0]) + " to Bot " + str(self.bot_give_high) + ".\n")
                a_bot_playground.add_bot(self.bot_give_high, self.chips.pop(0))
                # index_to_point = a_bot_playground.get_index_of_bot(self.bot_give_high)
                # a_bot_playground.bot_list[index_to_point].give_chips(a_bot_playground)
            tempfile.flush()
            
    def log_state(self):
        global tempfile
        if self.chips:
            tempfile.write("Bot " + str(self.bot_id) + " has chips " + str(self.chips) + ".\n")
    
class bot_playground:
    bot_list = []
    output_list = []
    def get_index_of_bot(self, id):
        if len(self.bot_list) == 0:
            return -1
        for index_result in range(0, len(self.bot_list)):
            if self.bot_list[index_result].bot_id == id:
                return index_result
        return -1
    def get_index_of_output(self, id):
        if len(self.output_list) == 0:
            return -1
        for index_result in range(0, len(self.output_list)):
            if self.output_list[index_result].output_id == id:
                return index_result
        return -1
    def add_bot(self, id, chip):
        bot_loc = self.get_index_of_bot(id)
        if bot_loc == -1:
            new_bot = bot(id, chip, -1, -1, False, False)
            self.bot_list.append(new_bot)
            return
        else:
            self.bot_list[bot_loc].add_chip(chip, self)
    def add_bot_with_instructions(self, id, give_low, give_high, give_output_low, give_output_high):
        bot_loc = self.get_index_of_bot(id)
        if bot_loc == -1:
            new_bot = bot(id, -1, give_low, give_high, give_output_low, give_output_high)
            self.bot_list.append(new_bot)
        else:
            self.bot_list[bot_loc].add_instructions(give_low, give_high, give_output_low, give_output_high)
    def run_all_bots_one_tick(self):
        self.bot_list.sort(key=lambda x: x.bot_id)
        self.output_list.sort(key=lambda x: x.output_id)
        for temp_bot in self.bot_list:
            temp_bot.log_state()
            temp_bot.give_chips(self)
        for temp_output in self.output_list:
            temp_output.log_state()
        # Add additional check for Output 0, 1, and 2:
        results = [self.get_index_of_output(0), self.get_index_of_output(1), self.get_index_of_output(2)]
        if results[0] != -1 and results[1] != -1 and results[2] != -1:
            result = self.output_list[results[0]].chips[0] * self.output_list[results[1]].chips[0] * self.output_list[results[2]].chips[0]
            print("The desired multiplication of the first elements in Output 0, 1, and 2 are: " + str(result))
            exit(0)
    def add_output(self, id, chip):
        if not self.output_list:
            new_output = output(id)
            new_output.add_chip(chip)
            self.output_list.append(new_output)
            return
        for output_index in range(0, len(self.output_list)):
            if self.output_list[output_index].output_id == id:
                index_to_return = output_index
                self.output_list[index_to_return].add_chip(chip)
                return
        new_output = output(id)
        new_output.add_chip(chip)
        self.output_list.append(new_output)

our_bot_playground = bot_playground()
with open("bot_instructions.txt", "r") as filestream:
    counter = 0
    for line in filestream:
        tempfile.write("Iteration " + str(counter) + ":\n")
        TEMP_LINE_INPUT = line.rstrip()
        if "value" in TEMP_LINE_INPUT:
            TEMP_LINE_INPUT = re.split(' ', TEMP_LINE_INPUT)
            # index 1 is width, 2 is height in TEMP_LINE_INPUT list
            tempfile.write("Bot " + TEMP_LINE_INPUT[5] + " acquired value " + TEMP_LINE_INPUT[1] + ".\n")
            our_bot_playground.add_bot(int(TEMP_LINE_INPUT[5]), int(TEMP_LINE_INPUT[1]))
        elif "gives low to" in TEMP_LINE_INPUT:
            TEMP_LINE_INPUT = re.split(' ', TEMP_LINE_INPUT)
            give_output_high = False
            give_output_low = False
            if "output" in TEMP_LINE_INPUT[5]:
                give_output_low = True
            if "output" in TEMP_LINE_INPUT[10]:
                give_output_high = True
            tempfile.write("Bot " + TEMP_LINE_INPUT[1] + " gives low to " + TEMP_LINE_INPUT[6] + " gives high to " + TEMP_LINE_INPUT[11] + ".\n")
            our_bot_playground.add_bot_with_instructions(int(TEMP_LINE_INPUT[1]), int(TEMP_LINE_INPUT[6]), int(TEMP_LINE_INPUT[11]), give_output_low, give_output_high)
        counter += 1
    while (True):
        our_bot_playground.run_all_bots_one_tick()
sys.stdout.flush()