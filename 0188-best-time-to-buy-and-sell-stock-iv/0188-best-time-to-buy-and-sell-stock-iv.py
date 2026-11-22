class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[0]*(k+1) for i in range(2)] for j in range(n+1)]

        for i in range(n-1,-1,-1):
            # temp = [[0]*3 for k in range(2)]
            for j in range(2):
                for lim in range(1,k+1):
                    if j == 1:
                        dp[i][j][lim] = max(-prices[i] + dp[i+1][0][lim],dp[i+1][1][lim])
                    else:
                        dp[i][j][lim] = max(prices[i] + dp[i+1][1][lim-1],dp[i+1][0][lim])
            # dp = temp

        return dp[0][1][k]
        