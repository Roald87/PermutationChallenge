"""
Solving Advent of Code 2020 day 1 part b:
In your expense report, what is the product of the three entries that sum to 2020?
"""

import itertools
import numpy as np

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

def roald2(fname):
    with open(fname) as f:
        data = f.readlines()
    data = [int(i) for i in data]

    for num1 in data:
        for num2 in set(data) - {num1}:
            for num3 in set(data) - {num1, num2}:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

def tom3(fname):
    with open(fname) as f:
        data = f.readlines()
    data = [int(i) for i in input]
    inp_len = len(data)
    data_array = np.zeros((inp_len, inp_len, inp_len))
    for x in range(np.shape(data_array)[0]):
        for y in range(np.shape(data_array)[1]):
            for z in range(np.shape(data_array)[2]):
                data_array[x, y, z] = data[x] + data[y] + data[z]
    indices = np.where(data_array == 2020)
    indices = set(indices[0])
    answer = 1
    for ind in indices:
        answer *= data[ind]
    return answer