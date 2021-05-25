class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
    
        word_queue = [s]
        while word_queue:
            word = word_queue.pop()
            n = len(word)
            for i in range(1, n+1):
                if word[:i] in word_set: 
                    if word[i:]: # there are letters left?
                        word_queue.append(word[i:])
                    else: # there are no letters left
                        return True
        return False         