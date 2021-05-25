class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        
        index_queue = [0]
        visited = set()
        while index_queue:
            start = index_queue.pop()
            if start in visited: 
                continue
            for i in range(start+1, n+1):
                if s[start:i] in word_set: 
                    if s[i:]: # there are letters left?
                        print(s[start:i] + ',' + s[i:] + ',' + str(i))
                        index_queue.append(i)
                    else: # there are no letters left
                        return True
            visited.add(start)
        return False      