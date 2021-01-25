import unittest
import time

from src.aoc_day1b import *


class AnswerCorrect(unittest.TestCase):
    methods = [
        tom1, roald1, tom2, roald2, tom3, roald3, tom4, roald4, roald5, roald6, roald7,
        roald8,
    ]
    filename = "aoc_20201b_input.txt"

    def test_check_answers(self):
        execution_times = {}
        for method in self.methods:
            start = time.process_time()
            answer = method(self.filename)
            elapsed_time = time.process_time() - start
            execution_times[method.__name__] = round(elapsed_time*1e3, 3)
            self.assertEqual(answer, 79734368, f"Method {method.__name__} failed")

        print("Execution times (ms):")
        sorted_execution_times = dict(sorted(execution_times.items(), key=lambda item: item[1]))

        for method, t in sorted_execution_times.items():
            print(f"{method}:\t{t}")

if __name__ == '__main__':
    unittest.main()
