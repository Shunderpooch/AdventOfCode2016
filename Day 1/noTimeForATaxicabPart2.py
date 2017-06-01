import sys
from enum import Enum


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

class Turn(Enum):
    Left = -1
    Right = 1

class Line:
    def __init__(self, starting_tuple, ending_tuple):
        self.starting_tuple = starting_tuple
        self.ending_tuple = ending_tuple

# Need a function that normalizes the state with the rest of the board (relative to absolute)
def axis_normalizer(current_direction, turn_dir):
    """ Normalizes a direction based on an indicated turn.
    """
    if current_direction == Direction.North and turn_dir == Turn.Left:
        new_direction = Direction.West
    elif current_direction == Direction.West and turn_dir == Turn.Right:
        new_direction = Direction.North
    else:
        new_direction = Direction(current_direction.value + turn_dir.value)
    return new_direction

def addToAxis(current_direction, amount_to_move, LOCATION_DIMENSIONS, ALL_LOCATIONS):
    for i in range(0, amount_to_move):
        if current_direction == Direction.North:
            LOCATION_DIMENSIONS[1] += 1
        elif current_direction == Direction.East:
            LOCATION_DIMENSIONS[0] += 1
        elif current_direction == Direction.South:
            LOCATION_DIMENSIONS[1] -= 1
        elif current_direction == Direction.West:
            LOCATION_DIMENSIONS[0] -= 1
        else:
            print("Something went wrong")
            exit(0)
        #if the location tuple is already in the list, we've found a match
        if (LOCATION_DIMENSIONS[0], LOCATION_DIMENSIONS[1]) in ALL_LOCATIONS:
            return True
        else:
            ALL_LOCATIONS.append((LOCATION_DIMENSIONS[0], LOCATION_DIMENSIONS[1]))
    return False

LINE_INPUT = []
INIT_DIRECTION = Direction.North
LOCATION_DIMENSIONS = [0, 0] # Format of X, Y coordinates
ALL_LOCATIONS = [(LOCATION_DIMENSIONS[0], LOCATION_DIMENSIONS[1])]

with open("input.txt", "r") as filestream:
    for line in filestream:
        TEMP_LINE_INPUT = line.split(', ')
        LINE_INPUT = TEMP_LINE_INPUT
sys.stdout.flush()


while LINE_INPUT: # Implicit boolean in the list having elements
    # Pop an element off the list
    ELEMENT = LINE_INPUT.pop(0)
    if ELEMENT[:1] == "L":
        INIT_DIRECTION = axis_normalizer(INIT_DIRECTION, Turn.Left)
    elif ELEMENT[:1] == "R":
        INIT_DIRECTION = axis_normalizer(INIT_DIRECTION, Turn.Right)
    else:
        print("Something went wrong")
        exit(1)
    if addToAxis(INIT_DIRECTION, int(ELEMENT[1:]), LOCATION_DIMENSIONS, ALL_LOCATIONS):
        print("Final Direction we were facing when we found the Easter Bunny's Hideout: " + INIT_DIRECTION.name)
        print("Final Coordinates of the Easter Bunny's Hideout (First one to visit twice): " + str(LOCATION_DIMENSIONS[0]) + "X, " 
            + str(LOCATION_DIMENSIONS[1]) + "Y")
        print(abs(LOCATION_DIMENSIONS[0]) + abs(LOCATION_DIMENSIONS[1]))
        exit(0)

print("There were no intersections at any point, so we can't find the Easter Bunny's Hideout")
