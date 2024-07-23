class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
            
        sorted_num = dict(sorted(d.items(), key = lambda x: (x[1],-x[0])))
        nums1= []
        for key,count in sorted_num.items():
            nums1 = nums1 + [key] * count
            
        return nums1