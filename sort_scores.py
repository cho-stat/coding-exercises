import unittest


def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time
    score_list = [0 for i in range(highest_possible_score)]
    
    for i in unsorted_scores: 
        
        score_list[i] += 1
    
    sorted_scores = [0 for i in unsorted_scores]
    
    idx = 0 
    
    for i in range(highest_possible_score):
        
        if score_list[highest_possible_score - i] > 0: 
            
            times = score_list[highest_possible_score - i]
            
            while times > 0:
                sorted_scores[idx] = highest_possible_score - i
                times += -1
                idx += 1
    
    return sorted_scores












# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)