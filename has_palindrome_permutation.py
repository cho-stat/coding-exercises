import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    # A permutation of the input is a palindrome if the count
    # of each letter is an even number except for at most one
    # letter, whose count can be odd. 
    
    # odd_count_set keeps track of which chars have an 
    # odd count. 
    
    odd_count_set = set()
    for letter in the_string:
        if letter in odd_count_set:
            odd_count_set.remove(letter)
        else:
            odd_count_set.add(letter)
    
    return False if len(odd_count_set) > 1 else True





# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)