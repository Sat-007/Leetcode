class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        result = []
        mapped = []
        
        for i,num in enumerate(nums):
            num = str(num)
            finalmapped = 0

            for n in num:
                finalmapped *= 10
                finalmapped += mapping[int(n)]
            result.append((finalmapped,i))
            
        result.sort()
        return [nums[p[1]] for p in result]
                
                
                
                
        