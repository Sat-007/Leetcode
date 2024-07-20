class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        dp = [[0] * n for _ in range(m)]

        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                dp[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= dp[i][j]
                colSum[j] -= dp[i][j]
        return dp