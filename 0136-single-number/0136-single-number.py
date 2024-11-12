class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        #print(count)
        for i, count in count.items():
            if count == 1:
                return i 
        return 0