class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] 
        
        while (len(output) <= n):
            output.extend([i+1 for i in output])
        return output [:n+1]