import unittest

def get_products_of_all_ints_except_at_index(int_list):

    # Take a list of integers and return a list of the products
    # e.g. given [1, 7, 3, 4]
    # produce [84, 12, 28, 21]
    # Rule: you cannot use division in your solution 

    n = len(int_list)
    
    product_list = [1 for x in int_list]
    i = 1
    while i < n: 
        product_list[i] = int_list[i-1]*product_list[i-1]
        i+=1
    
    after_prod = 1
    i = n-2
    while i >= 0:
        after_prod = after_prod * int_list[i+1]
        product_list[i] = after_prod*product_list[i]
        i += -1
    
    return product_list
    
    # time: n * n = O(n)
    # space: O(n) = O(n)








# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)