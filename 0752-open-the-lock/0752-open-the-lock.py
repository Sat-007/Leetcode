class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
        
        
        
        def helper(lock):
            res = [] 
            for i in range(4):
                digit = str ((int(lock[i]) + 1) % 10)  
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str ((int(lock[i]) - 1) % 10)  
                res.append(lock[:i] + digit + lock[i+1:])
            return res
            
            
            
            
        q = deque()
        q.append(["0000",0])
        visited = set(deadends)
       
        
        while q:
            lck, turns = q.popleft()
            if lck == target:
                return turns
            
            for i in helper(lck):
                if i not in visited:
                    visited.add(i)
                    q.append([i, turns + 1])
                    
        return -1 
                
                
            
            
            