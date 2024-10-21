class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = defaultdict (list)
        
        for char,cnt in count.items():
            bucket[cnt].append(char)
            
        res = ''
        for i in range(len(s), 0, -1):
            for c in bucket[i]:
                res += c*i
        return res