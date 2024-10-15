class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        i = 0
        j = 0 
        k = 0
        
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1
        length = len(res)
        #print(res)
        #print(len(res))
        if length % 2 == 0:
            return (res[length // 2 - 1] + res[length // 2]  ) / 2
            
        else:
            return res[length // 2]
            
        
            