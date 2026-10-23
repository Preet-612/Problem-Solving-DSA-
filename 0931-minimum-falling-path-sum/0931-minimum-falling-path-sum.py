class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        n = len(matrix)
        # dp = [[0] * n for _ in range(n)]
        prev = [0]*n
        # Base case: last row
        for j in range(n):
            prev[j] = matrix[n-1][j]

        # Fill the DP table from bottom to top
        for i in range(n-2, -1, -1):
            temp = [0]*n
            for j in range(n):
                down = matrix[i][j] + prev[j]

                leftd = matrix[i][j] + prev[j-1] if j > 0 else float('inf')

                rightd = matrix[i][j] + prev[j+1] if j < n-1 else float('inf')

                temp[j] = min(down, leftd, rightd)

            prev = temp

        # Minimum value in the first row
        return min(prev)


        # n = len(matrix)
        # # dp = [[0] * n for _ in range(n)]
        # prev = [0]*n
        # # Base case: last row
        # for j in range(n):
        #     dp[n-1][j] = matrix[n-1][j]

        # # Fill the DP table from bottom to top
        # for i in range(n-2, -1, -1):
        #     for j in range(n):
        #         down = matrix[i][j] + dp[i+1][j]

        #         leftd = matrix[i][j] + dp[i+1][j-1] if j > 0 else float('inf')

        #         rightd = matrix[i][j] + dp[i+1][j+1] if j < n-1 else float('inf')

        #         dp[i][j] = min(down, leftd, rightd)

        # # Minimum value in the first row
        # return min(dp[0])
        
        # n = len(matrix)
        # dp = [[-1]*n for i in range(n)]
        # def helper(i,j):
        #     if j < 0 or j >= n:
        #         return float('inf')

        #     if i == n-1:
        #         return matrix[i][j]

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     down = matrix[i][j] + helper(i+1,j) 
        #     leftd = matrix[i][j] + helper(i+1,j-1) 
        #     rightd = matrix[i][j] + helper(i+1,j+1) 

        #     dp[i][j] = min(down,leftd,rightd)
        #     return dp[i][j]

        # ans = float('inf')
        # for i in range(n):
            
        #     temp = helper(0,i)
        #     ans = min(temp,ans)
        
        # return ans
