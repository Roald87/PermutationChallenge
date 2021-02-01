"""
Lights in your grid are numbered from 0 to 999 in each direction;
the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
The instructions include whether to turn on, turn off,
or toggle various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle, inclusive;
a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.
After following the instructions, how many lights are lit?
"""
import numpy as np
import re

def tom1(instructions: list):
    def line_parser(line):
        expr = '(\w+) (\d+),(\d+) through (\d+),(\d+)'
        action, x1, y1, x2, y2 = re.search(expr, line).groups()
        return action, int(x1), int(y1), int(x2), int(y2)

    # define rectangle on 2 coord
    grid_pt1 = np.zeros((1000, 1000)) - 1  # start at -1 to indicate off
    for line in instructions:
        action, x1, y1, x2, y2 = line_parser(line)
        if action == 'on':
            grid_pt1[x1:x2 + 1, y1:y2 + 1] = 1

        elif action == 'off':
            grid_pt1[x1:x2 + 1, y1:y2 + 1] = -1

        elif action == 'toggle':
            grid_pt1[x1:x2 + 1, y1:y2 + 1] = -1 * grid_pt1[x1:x2 + 1, y1:y2 + 1]
    return np.sum(grid_pt1[grid_pt1 == 1])