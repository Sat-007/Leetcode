class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        
        keyMap = defaultdict(list)
        
        for i in range(len(keyName)):
            time = keyTime[i]
            name = keyName[i]
            
            t = time.replace(":", "")
            t = int(t)
            keyMap[name].append(t)
            
        ans = []
        
        for name, t in keyMap.items():
            t.sort()
            n = len(t)
            for i in range(n-2):
                if t[i+2] - t[i] <= 100:
                    ans.append(name)
                    break
            
        
        return sorted(ans)
        