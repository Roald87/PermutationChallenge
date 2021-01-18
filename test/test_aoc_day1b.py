import unittest

from src.aoc_day1b import *


class AnswerCorrect(unittest.TestCase):
    methods = [tom1]
    filename = "aoc_20201b_input.txt"

    def test_check_answer(self):
        for method in self.methods:
            self.assertEqual(method(self.filename), 79734368)


if __name__ == '__main__':
    unittest.main()
