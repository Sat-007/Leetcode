class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [[] for _ in range(target+1)]
        res [0] = [[]]
        
        for c in candidates:
            for i in range(c,target+1):
                for comb in res[i-c]:
                    res[i].append(comb + [c])
                    
        return res[target]