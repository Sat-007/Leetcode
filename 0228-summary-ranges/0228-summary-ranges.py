class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        int array nums
        range[a,b] set of int from a to b 
        return smallest sorted list of ranges
        
        input = [0,1,2,4,5,7]
        output ['0 -> 2, "4 - > 5", "7"]
        '''
        
        ans = []
        i = 0 
        while i < len(nums):
            begin = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i+1] - 1:
                i += 1
            end = nums[i]
            
            if begin == end:
                ans.append(str(begin))
            else:
                ans.append(str(begin) + '->' + str(end))
            
            i += 1
        return ans
        