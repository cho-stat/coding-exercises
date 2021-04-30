import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    m = 0 
    a = 0
    
    a_len = len(alices_list)
    m_len = len(my_list)
    
    if m_len == 0:
        return alices_list
    if a_len == 0:
        return my_list
    
    combined = []
    
    while len(my_list) > 0 or len(alices_list) > 0:
        if len(my_list) == 0:
            val = alices_list.pop(0)
        elif len(alices_list) == 0 or my_list[0] <= alices_list[0]:
            val = my_list.pop(0)
        else:
            val = alices_list.pop(0)
            
        combined.append(val)
            
    return combined



# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)