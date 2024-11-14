class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = defaultdict(list)
        in_degree = [0] * numCourses
        
        for c, p in prerequisites:
            prereqs[p].append(c) 
            in_degree[c] += 1
            
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0 ])
        order = []
        
        while q:
            course = q.popleft()
            order.append(course)
            
            for next_course in prereqs[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return order if len(order) == numCourses else []