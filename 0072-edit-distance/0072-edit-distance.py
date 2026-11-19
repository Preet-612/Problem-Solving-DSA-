class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        
        n = len(s1)
        m = len(s2)

        dp = [[-1]*(m+1) for i in range(n+1)]

        for j in range(m+1):              # it is for i == 0
            dp[0][j] = j
        
        for i in range(n+1):              # it is for j == 0
            dp[i][0] = i
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    ins = 1 + dp[i][j-1] #insert
                    dele = 1 + dp[i-1][j]   #delete
                    rep = 1 + dp[i-1][j-1]  #replace
                    dp[i][j] = min(ins,dele,rep)
        
        return dp[n][m]

        # def helper(i,j):

        #     if i == 0:
        #         return j
        #     if j == 0:
        #         return i
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s1[i-1] == s2[j-1]:
        #         dp[i][j] = 0 + helper(i-1,j-1)
        #     else:
            
        #         ins = 1 + helper(i,j-1) #insert
        #         dele = 1 + helper(i-1,j)   #delete
        #         rep = 1 + helper(i-1,j-1)  #replace
        #         dp[i][j] = min(ins,dele,rep)

        #     return dp[i][j]
        
        # return helper(n,m)























        # dp = [[-1]*(m) for i in range(n)]
        # def helper(i,j):

        #     if i < 0:
        #         return j+1
        #     if j < 0:
        #         return i+1
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     if s1[i] == s2[j]:
        #         dp[i][j] = 0 + helper(i-1,j-1)
        #     else:
            
        #         ins = 1 + helper(i,j-1) #insert
        #         dele = 1 + helper(i-1,j)   #delete
        #         rep = 1 + helper(i-1,j-1)  #replace
        #         dp[i][j] = min(ins,dele,rep)

        #     return dp[i][j]
        
        # return helper(n-1,m-1)