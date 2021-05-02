import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    # Use greedy approach to find the largest three ints 
    # Assuming here that all of the ints are positive 
    
    if len(list_of_ints) < 3: 
        raise Exception('too few ints')
    
    # Find smallest int by absolute value 
    def find_smallest(list_of_ints, absolute = False): 
        smallest = list_of_ints[0]
        if absolute: 
            for x in list_of_ints: 
                if abs(x) < abs(smallest): 
                    smallest = x 
        else: 
            smallest = min(list_of_ints)
        return smallest
        
        
    def find_product(list_of_ints): 
        prod = 1
        for x in list_of_ints: 
            prod = prod*x
        sign = 1 if prod >= 0 else -1
        return [abs(prod), sign]
    
    # Need to track the smallest int in a list of 3 
    largest_ints = list_of_ints[0:3]
    largest_absolute_ints = list_of_ints[0:3]
    
    smallest_int = find_smallest(largest_ints)
    smallest_abs_int = find_smallest(largest_absolute_ints, absolute=True)
    
    current_product, current_sign = find_product(largest_ints)
    current_abs_product, current_abs_sign = find_product(largest_absolute_ints)
    
    i = 3
    n = len(list_of_ints)
    
    while i < n: 
        if abs(list_of_ints[i]) > abs(smallest_abs_int): 
            idx = largest_absolute_ints.index(smallest_abs_int)
            largest_absolute_ints[idx] = list_of_ints[i]
            current_abs_product, current_abs_sign = find_product(largest_absolute_ints)
            smallest_abs_int = find_smallest(largest_absolute_ints, absolute=True)
            
        if list_of_ints[i] > smallest_int: 
            idx = largest_ints.index(smallest_int) 
            largest_ints[idx] = list_of_ints[i] 
            current_product, current_sign = find_product(largest_ints)
            smallest_int = find_smallest(largest_ints, absolute=False)
        
        i += 1
     
    return max({current_product*current_sign, current_abs_product*current_abs_sign})
    









# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)