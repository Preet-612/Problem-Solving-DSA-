class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        prev = [0]*m

        for j in range(m):
            prev[j] = triangle[m - 1][j]

        for i in range(m - 2, -1, -1):
            temp = [0]*m
            for j in range(i + 1):
                down = triangle[i][j] + prev[j]
                diagonal = triangle[i][j] + prev[j + 1]

                temp[j] = min(down, diagonal)
            prev = temp

        return prev[0]

        # m = len(triangle)
        # dp = [[-1]*m for i in range(m)]
        
        # def helper(i,j):
        #     if i == m-1:
        #         return triangle[i][j]
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     down = triangle[i][j] + helper(i+1,j)
        #     diagonal = triangle[i][j] + helper(i+1,j+1)
      
        #     dp[i][j] = min(down,diagonal)
        #     return dp[i][j]
        
        # return helper(0,0)        
        