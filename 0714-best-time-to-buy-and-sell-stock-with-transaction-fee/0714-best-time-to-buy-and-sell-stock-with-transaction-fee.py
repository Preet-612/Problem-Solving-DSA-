class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        
        n = len(prices)
        dp = [0]*2 

        for i in range(n-1,-1,-1):
            temp = [0]*2
            for j in range(2):
                if j == 0:
                    temp[j] = max(-prices[i] + dp[1],dp[0])
                else:
                    temp[j] = max((prices[i]-fee) + dp[0],dp[1])
            dp = temp
        return dp[0]

        # for i in range(n-1,-1,-1):
        #     for j in range(2):
        #         if j == 0:
        #             dp[i][j] = max(-prices[i] + dp[i+1][1],dp[i+1][0])
        #         else:
        #             dp[i][j] = max((prices[i]-fee) + dp[i+1][0],dp[i+1][1])
        # return dp[0][0]
        # def helper(i,j):

        #     if i == n:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     if j == 0:
        #         dp[i][j] = max(-prices[i] + helper(i+1,1),helper(i+1,0))
        #     else:
        #         dp[i][j] = max((prices[i]-fee) + helper(i+1,0),helper(i+1,1))
        #     return dp[i][j]
        
        # return helper(0,0)
