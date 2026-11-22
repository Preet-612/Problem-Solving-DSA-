class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0]*3 for i in range(2)]

        for i in range(n-1,-1,-1):
            temp = [[0]*3 for k in range(2)]
            for j in range(2):
                for lim in range(1,3):
                    if j == 1:
                        temp[j][lim] = max(-prices[i] + dp[0][lim],dp[1][lim])
                    else:
                        temp[j][lim] = max(prices[i] + dp[1][lim-1],dp[0][lim])
            dp = temp

        return dp[1][2]


        # n = len(prices)
        # dp = [[[-1]*3 for i in range(2)] for j in range(n)]
        # def helper(i,j,lim):

        #     if lim == 0:
        #         return 0
        #     if i == n:
        #         return 0
            
        #     if dp[i][j][lim] != -1:
        #         return dp[i][j][lim]
            
        #     if j == 1:
        #         dp[i][j][lim] = max(-prices[i] + helper(i+1,0,lim),helper(i+1,1,lim))
        #     else:
        #         dp[i][j][lim] = max(prices[i] + helper(i+1,1,lim-1),helper(i+1,0,lim))

        #     return dp[i][j][lim]
        
        # return helper(0,1,2)
