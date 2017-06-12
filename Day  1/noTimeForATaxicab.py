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

def addToAxis(current_direction, amount_to_move, LOCATION_DIMENSIONS):
    if current_direction == Direction.North:
        LOCATION_DIMENSIONS[1] += amount_to_move
    elif current_direction == Direction.East:
        LOCATION_DIMENSIONS[0] += amount_to_move
    elif current_direction == Direction.South:
        LOCATION_DIMENSIONS[1] -= amount_to_move
    elif current_direction == Direction.West:
        LOCATION_DIMENSIONS[0] -= amount_to_move

LINE_INPUT = []
INIT_DIRECTION = Direction.North
LOCATION_DIMENSIONS = [0, 0] # Format of X, Y coordinates

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
        exit()
    addToAxis(INIT_DIRECTION, int(ELEMENT[1:]), LOCATION_DIMENSIONS)
print("Final Direction: " + INIT_DIRECTION.name)
print("Final Coordinates: " + str(LOCATION_DIMENSIONS[0]) + "X, " 
    + str(LOCATION_DIMENSIONS[1]) + "Y")
print(abs(LOCATION_DIMENSIONS[0]) + abs(LOCATION_DIMENSIONS[1]))

