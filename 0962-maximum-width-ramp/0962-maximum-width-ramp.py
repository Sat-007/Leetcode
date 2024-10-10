class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        max_right = [0] * len(nums)
        prev_num = 0 
        i = len(nums) - 1
        
        for n in reversed(nums):
            max_right[i] = max(n,prev_num)
            prev_num = max_right[i]
            i -= 1
            
        res = 0 
        l = 0 
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            res = max(res, r-l)
        return res