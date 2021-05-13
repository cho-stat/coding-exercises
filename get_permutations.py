import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    string_list = list(string)
    
    if len(string_list) == 2: 
        all_perms = [string_list[-1::-1], string_list]
        all_perms_string = {''.join(x) for x in all_perms}
        return all_perms_string
        
    elif len(string_list) <= 1: 
        return { string }
        
    else: 
        all_perms = set()
        for letter in string_list:
            letter_perm_set = get_permutations(''.join([x for x in string_list if x != letter]))
            for perm in letter_perm_set: 
                all_perms.add(letter + perm)
        return all_perms


















  # Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)