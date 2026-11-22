class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)
        dp = [[-1]*2 for i in range(n)]
        def helper(i,j):

            if i >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if j == 1:
                dp[i][j] = max(-prices[i] + helper(i+1,0),helper(i+1,1))
            else:
                dp[i][j] = max(prices[i] + helper(i+2,1),helper(i+1,0))
            
            return dp[i][j]

        return helper(0,1)