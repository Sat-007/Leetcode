class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = {num:True for num in nums}
        missing = []
        n = len(nums)
        for i in range(1, n +1):
            if i not in num_set:
                missing.append(i)
                
        return missing