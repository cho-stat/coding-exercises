import unittest


def find_repeat(numbers):
    
    n = len(numbers)
    floor_int = min(numbers)
    ceil_int = max(numbers)

    while ceil_int - floor_int > 0:     
        midpt = (floor_int + ceil_int) // 2
        left_count = 0
    
        for i in numbers: 
            if i <= midpt and i >= floor_int: 
                left_count += 1
    
        if left_count > (midpt - floor_int + 1): 
            ceil_int = midpt
        else:
            floor_int = midpt + 1
        
    return floor_int









# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)