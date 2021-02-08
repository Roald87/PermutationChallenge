import unittest
import time
from inspect import getmembers, isfunction

import src.fizzbuzz

expected = (
    "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 "
    + "Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz"
)


class MyTestCase(unittest.TestCase):

    methods = [member[1] for member in getmembers(src.fizzbuzz, isfunction)]

    def test_check_answers(self):
        execution_times = {}
        for method in self.methods:
            start = time.process_time()
            answer = method()
            elapsed_time = time.process_time() - start
            execution_times[method.__name__] = round(elapsed_time * 1e3, 3)
            self.assertEqual(expected, answer, f"Method {method.__name__} failed")

        print("Execution times FizzBuzz (ms):")
        sorted_execution_times = dict(
            sorted(execution_times.items(), key=lambda item: item[1])
        )

        for method, t in sorted_execution_times.items():
            print(f"{method}:\t{t}")


if __name__ == "__main__":
    unittest.main()
