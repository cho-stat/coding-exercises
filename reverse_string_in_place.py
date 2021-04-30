import unittest

# Q: Write a function that takes a list of characters 
# and reverses the letters in place


def reverse(list_of_chars):
    n = len(list_of_chars)
    i = 0
    
    while i < n-i-1:
        left = list_of_chars[i] 
        right = list_of_chars[n-i-1]
        list_of_chars[i] = right
        list_of_chars[n-i-1] = left
        i += 1 

    pass





# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)