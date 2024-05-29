class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx = 0 
        num_zeroes = 0
        l = 0 
        for r in range(len(nums)):
            if nums[r] == 0 :
                num_zeroes += 1
                
            while num_zeroes > k:
                if nums[l] == 0 :
                    num_zeroes -= 1
                l += 1
            w = r - l + 1
            maxx = max(maxx,w)
            
        return maxx
            