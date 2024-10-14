class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 :
            return 0
        if n < 3 : return 1
        
        dp = [0] * (n+1)
        i = 3
        dp[1] = dp[2] = 1
        while i <= n:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            i += 1
            
        return dp[n]
        