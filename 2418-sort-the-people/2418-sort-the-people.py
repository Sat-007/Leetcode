class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        seen = {}
        
        for n,h in zip(names,heights):
            seen[h] = n
            
        res = []
        
        for h in reversed(sorted(heights)):
            res.append(seen[h])
        return res
        