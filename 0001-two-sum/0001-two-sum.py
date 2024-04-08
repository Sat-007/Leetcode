class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        CM = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in CM:
                return [CM[num],i]
            else:
                CM[complement] = i 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  