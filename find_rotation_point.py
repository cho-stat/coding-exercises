import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    floor_index = 0
    ceiling_index = len(words) - 1
    
    while ceiling_index - floor_index > 1:
        
        halfway = (floor_index + ceiling_index) // 2
        
        if words[halfway] > words[0]:
            # rotation point is to the right of halfway point
            floor_index = halfway 
        
        else:
            # rotation point is to the left of halfway point
            ceiling_index = halfway 

    return ceiling_index 








# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)