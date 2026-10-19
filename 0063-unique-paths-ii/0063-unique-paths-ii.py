class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for i in range(m)] 
        def helper(i,j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = helper(i,j-1) + helper(i-1,j)
            return dp[i][j]
            
        return helper(m-1,n-1)
            
            