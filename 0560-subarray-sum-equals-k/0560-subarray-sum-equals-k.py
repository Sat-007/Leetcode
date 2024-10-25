class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        cur = 0 
        prefixS = {0:1}
        for n in nums:
            cur += n 
            diff = cur - k 
            res+= prefixS.get(diff,0)
            prefixS[cur] = 1 + prefixS.get(cur,0)
        return res