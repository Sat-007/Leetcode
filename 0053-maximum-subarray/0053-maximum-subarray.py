class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        summ = 0 
        
        for i in range(len(nums)):
            summ += nums[i]
            ans = max(ans,summ)
            
            if summ < 0 :
                summ = 0 
                
        return ans