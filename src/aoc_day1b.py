"""
Solving Advent of Code 2020 day 1 part b:
In your expense report, what is the product of the three entries that sum to 2020?
"""

import itertools

def tom1(fname):
    f = open(fname,'r')
    input = f.readlines()
    input = [int(line.strip()) for line in input]
    f.close()

    for n1 in range(len(input)):
        for n2 in range(len(input)):
            for n3 in range(len(input)):
                if n1 < n2 and n1 < n3 and n2 < n3:
                    val1 = input[n1]
                    val2 = input[n2]
                    val3 = input[n3]
                    if val1+val2+val3 == 2020:
                        return val1*val2*val3

def roald1(fname):
    with open(fname) as f:
        data = f.readlines()
    data = map(int, data)

    for nums in itertools.combinations(data, 3):
        if sum(nums) == 2020:
            return nums[0] * nums[1] * nums[2]

def tom2(fname):
    f = open(fname, 'r')
    input = f.readlines()
    input = [int(line.strip()) for line in input]
    f.close()
    sumvals = [x*y*z for x in input for y in input for z in input if x+y+z == 2020]
    return sumvals[0]