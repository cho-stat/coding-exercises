import unittest


def find_rotation_point(words):
    
    def find_point(words, floor_index, ceiling_index): 
        
        if ceiling_index - floor_index > 1: 
  
            halfway = (floor_index + ceiling_index) // 2
        
            if words[halfway] < words[floor_index]: 
                # rotation point must be between floor_index & halfway
                return find_point(words, floor_index, halfway)
        
            if words[halfway] > words[ceiling_index]: 
                # rotation point be between halfway and ceiling_index
                return find_point(words, halfway, ceiling_index)    
        else: 
            # only two words to compare: floor and ceiling
            # determine which one is the rotation point 
        
            if words[floor_index] < words[ceiling_index]:
                return floor_index
            else: 
                return ceiling_index
                
    return find_point(words, 0, len(words) - 1)








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