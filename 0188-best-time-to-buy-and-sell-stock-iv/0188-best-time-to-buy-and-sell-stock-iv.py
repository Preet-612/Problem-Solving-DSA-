class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0]*(k+1) for i in range(2)]

        for i in range(n-1,-1,-1):
            temp = [[0]*(k+1) for l in range(2)]
            for j in range(2):
                for lim in range(1,k+1):
                    if j == 1:
                        temp[j][lim] = max(-prices[i] + dp[0][lim],dp[1][lim])
                    else:
                        temp[j][lim] = max(prices[i] + dp[1][lim-1],dp[0][lim])
            dp = temp

        return dp[1][k]
        