class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        dp = [[0]*n for i in range(m)]
        dp[m-1][n-1] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left

        
        return dp[m-1][n-1]
        # def helper(i, j):

        #     # Reached destination
        #     if i == m - 1 and j == n - 1:
        #         return 1

        #     # Out of boundary
        #     if i >= m or j >= n:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     # Move Down + Move Right
        #     down = helper(i + 1, j)
        #     right = helper(i, j + 1)

        #     dp[i][j] = down + right
        #     return dp[i][j]
        # return helper(0, 0)