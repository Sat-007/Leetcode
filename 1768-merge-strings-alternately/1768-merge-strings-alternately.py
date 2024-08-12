class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        
        i, j = 0, 0 
        res = '' 
        while i < m or j < n :
            res += word1[i] if i < m else ""
            res += word2[j] if j < n else ""
            i += 1
            j += 1
            
        return res