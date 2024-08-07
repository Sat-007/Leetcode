class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        
        for c, p in prerequisites:
            prereqs[c].append(p)
            
        seen = set()
        
        def helper(course,seen):
            if course in seen:
                return True
            seen.add(course)
            for p in prereqs[course]:
                if helper(p,seen):
                    return True
            prereqs[course] = []
            seen.remove(course)
            return False
            
            
            
        for course in range(numCourses):
            if helper(course,seen):
                return False  
        return True
    