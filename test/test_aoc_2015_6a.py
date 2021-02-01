import os
import unittest
import time
from inspect import getmembers, isfunction

import src.aoc_2015_6a as aoc_2015_6a

def get_instructions(filename):
    with open(filename) as f:
        data = f.readlines()
        data = [line.strip() for line in data]
    return data


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
instructions = get_instructions(os.path.join(THIS_DIR, "aoc_2015_6a_input.txt"))


class MyTestCase(unittest.TestCase):

    methods = [member[1] for member in getmembers(aoc_2015_6a, isfunction)]

    def test_check_answers(self):
        execution_times = {}
        for method in self.methods:
            start = time.process_time()
            answer = method(instructions)
            elapsed_time = time.process_time() - start
            execution_times[method.__name__] = round(elapsed_time * 1e3, 3)
            self.assertEqual(377891, answer, f"Method {method.__name__} failed")

        print("Execution times AoC 2015 day 6 part a (ms):")
        sorted_execution_times = dict(
            sorted(execution_times.items(), key=lambda item: item[1])
        )

        for method, t in sorted_execution_times.items():
            print(f"{method}:\t{t}")


if __name__ == "__main__":
    unittest.main()