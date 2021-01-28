import os
import unittest
import time
from inspect import getmembers, isfunction

import src.aoc_2020_1b as aoc_2020_1b

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class AnswerCorrect(unittest.TestCase):

    methods = [member[1] for member in getmembers(aoc_2020_1b, isfunction)]
    filename = os.path.join(THIS_DIR, "aoc_2020_1b_input.txt")

    def test_check_answers(self):
        execution_times = {}
        for method in self.methods:
            start = time.process_time()
            answer = method(self.filename)
            elapsed_time = time.process_time() - start
            execution_times[method.__name__] = round(elapsed_time * 1e3, 3)
            self.assertEqual(79734368, answer, f"Method {method.__name__} failed")

        print("Execution times AoC 2020 day 1 part b (ms):")
        sorted_execution_times = dict(
            sorted(execution_times.items(), key=lambda item: item[1])
        )

        for method, t in sorted_execution_times.items():
            print(f"{method}:\t{t}")


if __name__ == "__main__":
    unittest.main()
