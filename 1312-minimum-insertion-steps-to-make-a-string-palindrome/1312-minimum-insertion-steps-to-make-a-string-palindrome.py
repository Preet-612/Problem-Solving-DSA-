class Solution:
    def minInsertions(self, s: str) -> int:
        # Space optimization

        n = len(s)
        s2 = s[::-1]
        dp = [0] * (n+1) 
        for i in range(1,n+1):
            temp = [0]*(n+1)
            for j in range(1,n+1):
                if s[i-1] == s2[j-1]:
                    temp[j] = 1 + dp[j-1]
                else:
                    temp[j] = max(dp[j],temp[j-1])
            
            dp = temp

        return n - dp[n]


        #Tabulation code

        
        
        
        
        
        
        # n = len(s)
        # s2 = s[::-1]
        # dp = [[0] * (n+1) for i in range(n+1)]
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         if s[i-1] == s2[j-1]:
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        # return n - dp[n][n]


        # def helper(i,j):

        #     if i == 0 or j == 0:
        #         return 0
            
        #     if s[i-1] == s2[j-1]:
        #         return 1 + helper(i-1,j-1)
            
        #     return max(helper(i-1,j),helper(i,j-1))
        
        # t = helper(n,n)

        # return n - t