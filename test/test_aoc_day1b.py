import unittest

from src.aoc_day1b import *


class AnswerCorrect(unittest.TestCase):
    methods = [tom1, roald1,tom2]
    filename = "aoc_20201b_input.txt"

    def test_check_answers(self):
        for method in self.methods:
            self.assertEqual(method(self.filename), 79734368, f"Method {method.__name__} failed")


if __name__ == '__main__':
    unittest.main()
