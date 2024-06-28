class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        v=sorted(strs)
        a=""
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return a
            a+=first[i]
        return a