class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        summ = sum(a for a in nums if a % 2 == 0)
        
        for val , i in queries:
            if nums[i] % 2 == 0:
                summ -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                summ += nums[i]
            ans.append(summ)
        return ans