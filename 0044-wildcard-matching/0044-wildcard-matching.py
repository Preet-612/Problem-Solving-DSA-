class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)
        dp = [False] * (m+1) 

        dp[0] = True

        for j in range(1, m+1):
            if p[j-1] == '*':
                dp[j] = dp[j-1]

        for i in range(1, n+1):
            temp = [False] * (m+1)
            for j in range(1, m+1):

                if s[i-1] == p[j-1] or p[j-1] == '?':
                    temp[j] = dp[j-1]

                elif p[j-1] == '*':
                    temp[j] = temp[j-1] or dp[j]
                
            dp = temp

        return dp[m]


        # dp = [[False] * (m+1) for _ in range(n+1)]

        # dp[0][0] = True

        # for j in range(1, m+1):
        #     if p[j-1] == '*':
        #         dp[0][j] = dp[0][j-1]

        # for i in range(1, n+1):
        #     for j in range(1, m+1):

        #         if s[i-1] == p[j-1] or p[j-1] == '?':
        #             dp[i][j] = dp[i-1][j-1]

        #         elif p[j-1] == '*':
        #             dp[i][j] = dp[i][j-1] or dp[i-1][j]

        # return dp[n][m]



        # dp = [[-1]*m for i in range(n)]
        # def helper(i,j):

        #     if i < 0 and j < 0:
        #         return True
        #     if j < 0 and i >= 0:
        #         return False
        #     if i < 0 and j >= 0:
        #         for k in range(j+1):
        #             if p[k] != "*":
        #                 return False
        #         return True
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s[i] == p[j] or p[j] == "?":
        #         dp[i][j] =  helper(i-1,j-1)
        #     elif p[j] == "*":
        #         dp[i][j] = helper(i-1,j) or helper(i,j-1)
        #     else:
        #         dp[i][j] = False
        #     return dp[i][j]
        
        # return helper(n-1,m-1)