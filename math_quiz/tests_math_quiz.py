import unittest
from math_quiz import get_random_integer, get_operation, compute


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_operation(self):
        # Test if random operation generated are among +, -, *
        for _ in range(1000):
             operator = get_operation()
             self.assertTrue(operator=='+'or operator == '-' or operator == '*')
        

    def test_compute(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (6, 1, '-', '6-1', 5), (7, 3, '*', '7 * 3', 21),
                (7, 5, '+', '7 + 5', 12), (8, 4, '-', '8 - 4', 4), (9, 0, '*', '9 * 0', 0)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                question, result = compute(num1, num2, operator)
                self.assertTrue(expected_problem== question and expected_answer == result)

if __name__ == "_main_":
    unittest.main()