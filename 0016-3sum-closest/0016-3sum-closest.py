class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        closest = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i + 1
            high = n - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                
                if abs(s-target) < abs(closest-target):
                    closest = s 
                
                if s == target:
                    return s
                
                if s < target:
                    low += 1
                else:
                    high -= 1
                    
        return closest
                    
        