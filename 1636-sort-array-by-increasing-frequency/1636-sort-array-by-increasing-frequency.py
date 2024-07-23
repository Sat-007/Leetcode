class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num,0) + 1
            
        sorted_num = dict(sorted(num_count.items(), key = lambda x: (x[1],-x[0])))
        nums1= []
        for key,count in sorted_num.items():
            nums1 = nums1 + [key] * count
            
        return nums1