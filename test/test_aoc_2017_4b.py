import os
import unittest
import time
from inspect import getmembers, isfunction

import src.aoc_2017_4b as aoc_2017_4b

def get_passphrases(filename):
    with open(filename) as f:
        data = f.read().splitlines()

    return data

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
passphrases = get_passphrases(os.path.join(THIS_DIR, "aoc_2017_4b_input.txt"))

class MyTestCase(unittest.TestCase):

    methods = [member[1] for member in getmembers(aoc_2017_4b, isfunction)]

    def test_check_answers(self):
        execution_times = {}
        for method in self.methods:
            start = time.process_time()
            answer = method(passphrases)
            elapsed_time = time.process_time() - start
            execution_times[method.__name__] = round(elapsed_time * 1e3, 3)
            self.assertEqual(answer, 186, f"Method {method.__name__} failed")

        print("Execution times (ms):")
        sorted_execution_times = dict(sorted(execution_times.items(), key=lambda item: item[1]))

        for method, t in sorted_execution_times.items():
            print(f"{method}:\t{t}")


if __name__ == '__main__':
    unittest.main()
