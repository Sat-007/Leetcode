class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        map_ = {}
        for t in target:
            if t in map_:
                map_[t] += 1
            else:
                map_[t] = 1
        
        
        for a in arr:
            if a in map_ and map_[a] > 0:
                map_[a] -= 1
            else:
                return False
            
        return True