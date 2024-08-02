class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        l = 0 
        ones_window = max_window_ones = 0
        
        for r in range(2*n):
            if nums[r % n ]:
                ones_window += 1
            
            if r - l + 1 > ones:
                ones_window -= nums[l%n]
                l += 1
                
            max_window_ones = max(max_window_ones,ones_window)
            
            
            
        
        
        return ones - max_window_ones