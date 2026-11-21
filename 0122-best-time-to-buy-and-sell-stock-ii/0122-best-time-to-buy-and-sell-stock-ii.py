class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)
        
        dp = [[0]*2 for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j == 0:                   # buy
                    tk = -prices[i] + dp[i+1][1]
                    ntk = dp[i+1][0]
                else:                               # sell
                    tk = prices[i] + dp[i+1][0]
                    ntk = dp[i+1][1]
                dp[i][j] = max(tk,ntk)
        
        return dp[0][0]

                       


        # dp = [[-1]*2 for i in range(n)]
        # def helper(i,j):
            
        #     if i == n:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if j == 0:                   # buy
        #         tk = -prices[i] + helper(i+1,1)
        #         ntk = helper(i+1,0)
        #     else:                               # sell
        #         tk = prices[i] + helper(i+1,0)
        #         ntk = helper(i+1,1)
            
        #     dp[i][j] = max(tk,ntk)
        #     return dp[i][j]
        
        # return helper(0,0)
                
