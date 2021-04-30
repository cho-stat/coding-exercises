import unittest


def reverse_words(message):
    # Illustration of process: 
    #  message = ["m", "u", "c", 'h", " ", "t", "o", "o"]
    #  --> ["o", "o", "t", " ", "h", "c", "u", "m"]
    #  --> ["t", "o", "o", " ", "m", "u", "c", "h"] 


    # Function for reversing all of the characters
    def reverse_chars(list_of_chars):
        i = 0
        j = len(list_of_chars) - 1
    
        while i < j:
            list_of_chars[i], list_of_chars[j] = list_of_chars[j], list_of_chars[i]
            i+=1
            j+=-1
            
        return list_of_chars
    
    # Reverse all of the characters in the list of chars
    message = reverse_chars(message)
    
    n = len(message)
    word_start = 0
    word_end = 0
    
    # Re-reverse (i.e. return to original order) the characters of words
    while word_end <= n:
        if word_end == n or message[word_end] == ' ':
            message[word_start:word_end] = reverse_chars(message[word_start:word_end])
            word_start = word_end + 1
            word_end = word_start 
    
        else:
            word_end += 1 

    pass







# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)