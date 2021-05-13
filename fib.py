import unittest


def fib(n):

    # Compute the nth Fibonacci number
    if n < 0: 
        raise Exception('n is negative')
        
    if n in {0, 1}: 
        # base case
        return n 
    else: 
        fib_minus_1 = 1
        fib_minus_2 = 0
        for i in range(n+1)[2:]: 
            fib = fib_minus_2 + fib_minus_1
            fib_minus_2 = fib_minus_1
            fib_minus_1 = fib 
        return fib 


















# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)