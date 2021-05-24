class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) < len(nums2): 
            num_set = {num for num in nums1} 
            compare_list = nums2
        else: 
            num_set = {num for num in nums2}
            compare_list = nums1
        
        result = set()
    
        for num in compare_list: 
            if num in num_set and num not in result: 
                result.add(num) 
       
        return [num for num in result]