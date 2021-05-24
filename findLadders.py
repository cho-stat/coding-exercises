class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def is_neighbor(word1, word2): 
            # assume word1 and word 2 are same length
            diff = 0
            for idx in range(len(word1)):
                if word1[idx] != word2[idx]:
                    diff += 1
                    if diff > 1: 
                        return False
            return True if diff == 1 else False 
    
        queue = [(beginWord, [beginWord], 0)]
        paths = []
        max_distance = float('Inf')
    
        while queue: 
            current_word, current_path, distance = queue.pop()
            if distance > max_distance: 
                continue 
            else: 
                neighbor_list = [word for word in wordList if is_neighbor(word, current_word) and word not in current_path]
                if endWord in neighbor_list: 
                    current_path.append(endWord) 
                    paths.append((current_path, distance))
                    max_distance = min(distance, max_distance)
                else:
                    for neighbor in neighbor_list:
                        queue.append((neighbor, current_path + [neighbor], distance+1))

    
        return [path for path, distance in paths if distance == max_distance]