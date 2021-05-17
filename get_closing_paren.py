import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    # Use a stack: add parenths at opening_paren_index to stack
    # Add to stack for opening parens
    # Pop from stack for close parens
    # If stack reaches 0 length from a pop operation, you have
    # reached the matching close parens. 
    # If you iterate through the whole sentence and fail
    # to find a match, you have an unmatched parens, raise exception
    
    tracker = 0
    for i in range(opening_paren_index, len(sentence)+1): 
        if sentence[i] == '(':
            tracker += 1
        elif sentence[i] == ')':
            tracker -= 1
            if tracker == 0: 
                return i 
        else: 
            continue 
        
    raise Exception("match not found")


















# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)