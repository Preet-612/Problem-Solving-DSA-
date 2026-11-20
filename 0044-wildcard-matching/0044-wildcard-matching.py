class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n = len(s)
        m = len(p)
        dp = [[-1]*m for i in range(n)]
        def helper(i,j):

            if i < 0 and j < 0:
                return True
            if j < 0 and i >= 0:
                return False
            if i < 0 and j >= 0:
                for k in range(j+1):
                    if p[k] != "*":
                        return False
                return True
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == p[j] or p[j] == "?":
                dp[i][j] =  helper(i-1,j-1)
            elif p[j] == "*":
                dp[i][j] = helper(i-1,j) or helper(i,j-1)
            else:
                dp[i][j] = False
            return dp[i][j]
        
        return helper(n-1,m-1)