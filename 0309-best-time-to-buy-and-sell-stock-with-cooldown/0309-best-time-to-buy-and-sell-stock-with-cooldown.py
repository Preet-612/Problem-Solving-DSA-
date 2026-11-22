class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        n = len(prices)
        
        dp = [0]*2 
        dp2 = [0]*2
        for i in range(n-1,-1,-1):
            temp = [0]*2
            for j in range(2):
                if j == 1:
                    temp[j] = max(-prices[i] + dp[0],dp[1])
                else:
                    temp[j] = max(prices[i] + dp2[1],dp[0])
            dp2 = dp
            dp = temp

        return dp[1]
               
        #tabulation

        # dp = [[0]*2 for i in range(n+2)]
        # for i in range(n-1,-1,-1):
        #     for j in range(2):
        #         if j == 1:
        #             dp[i][j] = max(-prices[i] + dp[i+1][0],dp[i+1][1])
        #         else:
        #             dp[i][j] = max(prices[i] + dp[i+2][1],dp[i+1][0])
        # return dp[0][1]


        # space optimization

        # dp = [[-1]*2 for i in range(n)]
        # def helper(i,j):

        #     if i >= n:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if j == 1:
        #         dp[i][j] = max(-prices[i] + helper(i+1,0),helper(i+1,1))
        #     else:
        #         dp[i][j] = max(prices[i] + helper(i+2,1),helper(i+1,0))
            
        #     return dp[i][j]

        # return helper(0,1)