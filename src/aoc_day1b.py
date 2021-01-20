"""
Solving Advent of Code 2020 day 1 part b:
In your expense report, what is the product of the three entries that sum to 2020?
"""

import itertools
import numpy as np

def tom1(fname):
    f = open(fname,'r')
    numbers = f.readlines()
    numbers = [int(line.strip()) for line in numbers]
    f.close()

    for n1 in range(len(numbers)):
        for n2 in range(len(numbers)):
            for n3 in range(len(numbers)):
                if n1 < n2 and n1 < n3 and n2 < n3:
                    val1 = numbers[n1]
                    val2 = numbers[n2]
                    val3 = numbers[n3]
                    if val1+val2+val3 == 2020:
                        return val1*val2*val3

def roald1(fname):
    with open(fname) as f:
        numbers = f.readlines()
    numbers = map(int, numbers)

    for nums in itertools.combinations(numbers, 3):
        if sum(nums) == 2020:
            return nums[0] * nums[1] * nums[2]

def tom2(fname):
    f = open(fname, 'r')
    numbers = f.readlines()
    numbers = [int(line.strip()) for line in numbers]
    f.close()
    sumvals = [x*y*z for x in numbers for y in numbers for z in numbers if x+y+z == 2020]
    return sumvals[0]

def roald2(fname):
    with open(fname) as f:
        numbers = f.readlines()
    numbers = [int(i) for i in numbers]

    for num1 in numbers:
        for num2 in set(numbers) - {num1}:
            for num3 in set(numbers) - {num1, num2}:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

def tom3(fname):
    with open(fname) as f:
        numbers = f.readlines()
    numbers = [int(i) for i in numbers]
    inp_len = len(numbers)
    data_array = np.zeros((inp_len, inp_len, inp_len))
    for x in range(np.shape(data_array)[0]):
        for y in range(np.shape(data_array)[1]):
            for z in range(np.shape(data_array)[2]):
                data_array[x, y, z] = numbers[x] + numbers[y] + numbers[z]
    indices = np.where(data_array == 2020)
    indices = set(indices[0])
    answer = 1
    for ind in indices:
        answer *= numbers[ind]
    return answer

def roald3(fname):
    with open(fname) as f:
        numbers = list(map(int, f.readlines()))

    numbers.sort()

    for num1 in numbers:
        for num2 in reversed(numbers):
            for num3 in numbers:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3