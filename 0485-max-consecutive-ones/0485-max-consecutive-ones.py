class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        maxCount = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                count += nums[i]
                maxCount = max(count,maxCount)

            else:
                count = 0 

        return maxCount