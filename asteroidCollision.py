class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # (1, -1) -> collision
        # (-1, 1), (-1, -1), (1, 1) -> no collision
        
        return_list = []
        asteroids.reverse()
        
        while len(asteroids) > 0: 
            if len(return_list) == 0 or not (return_list[-1] > 0 and asteroids[-1] < 0):
                # no collision 
                # add the astrd to the list 
                return_list.append(asteroids[-1]) 
                asteroids.pop()
            else: 
                if abs(return_list[-1]) > abs(asteroids[-1]): 
                    # previous asteroid overtakes candidate asteroid
                    # list remains unchanged, move on to next asteroid
                    asteroids.pop()
                elif abs(return_list[-1]) == abs(asteroids[-1]):
                    # both asteroids explode
                    return_list.pop()
                    asteroids.pop()
                else: 
                    # candidate asteroid overtakes previous asteroid
                    # index does not advance in case candidate asteroid
                    # also overtakes other previously added asteroids
                    return_list.pop() 
        
        return return_list