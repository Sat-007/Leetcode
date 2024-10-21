class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        times = defaultdict(list)
        
        for i in range(n):
            time = keyTime[i]
            name = keyName[i]
            
            t = time.split(":")
            h = int(t[0])
            m = int(t[1])
            times[name].append(h*60+m)
            
        ans = []
        
        for name in times:
            times_list = sorted(times[name])
            
            queue = deque()
            for t in times_list:
                queue.append(t)
                
                while t - queue[0] > 60:
                    queue.popleft()
                
                if len(queue) >= 3:
                    ans.append(name)
                    break
                    
        return sorted(ans)
            