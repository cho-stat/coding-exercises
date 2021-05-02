import unittest
import re

class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
         words = re.findall('[a-zA-Z]+', input_string.lower())
         self.words_to_counts = {}
         for word in words: 
            if word in self.words_to_counts: 
                self.words_to_counts[word] += 1
            else: 
                self.words_to_counts[word] = 1