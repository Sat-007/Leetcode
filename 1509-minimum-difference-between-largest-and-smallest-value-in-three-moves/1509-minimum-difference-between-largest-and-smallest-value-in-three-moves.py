class Solution:
    def minDifference(self, nums: List[int]) -> int:
        res = float ('inf')
        
        if len(nums) <= 4:
            return 0 
        
        
        min_values = sorted(heapq.nsmallest(4,nums))
        max_values = sorted(heapq.nlargest(4,nums))
        
        
        for i in range(4):
            res = min (res, max_values[i] - min_values[i])
        return res
        