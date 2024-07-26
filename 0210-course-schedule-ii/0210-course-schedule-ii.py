class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        res = []
        prereqs = defaultdict(list)
        for c,p in prerequisites:
            prereqs[c].append(p)
            
        
        seen, cycle = set(), set()
        
        def dfs(c):
            if c in cycle:
                return False
            if c in seen: 
                return True
            
            cycle.add(c)
            
            for pre in prereqs[c]:
                if dfs(pre) == False:
                    return False
                
            seen.add(c)    
            cycle.remove(c)    
            res.append(c)    
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
            
        return res