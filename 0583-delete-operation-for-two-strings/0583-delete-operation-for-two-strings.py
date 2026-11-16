class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[-1]*(m+1) for i in range(n+1)]
        def helper(i,j):

            if i == 0 or j == 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + helper(i-1,j-1)
            else:
                dp[i][j] =  max(helper(i-1,j),helper(i,j-1))

            return dp[i][j]
        t = helper(n,m)
        a = n - t
        b = m - t
        return a + b