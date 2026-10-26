class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]

        def helper(i, j1, j2):
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')

            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]

            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            ans = float('-inf')

            for d1 in range(-1, 2):
                for d2 in range(-1, 2):
                    ans = max(
                        ans,
                        helper(i + 1, j1 + d1, j2 + d2)
                    )

            if j1 == j2:
                ans += grid[i][j1]
            else:
                ans += grid[i][j1] + grid[i][j2]

            dp[i][j1][j2] = ans
            return dp[i][j1][j2]

        return helper(0, 0, m - 1)


# class Solution:
#     def cherryPickup(self, grid: list[list[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])

#         dp = [[[0] * m for _ in range(m)] for _ in range(n)]

#         for j1 in range(m):
#             for j2 in range(m):
#                 if j1 == j2:
#                     dp[n - 1][j1][j2] = grid[n - 1][j1]
#                 else:
#                     dp[n - 1][j1][j2] = (
#                         grid[n - 1][j1] + grid[n - 1][j2]
#                     )

#         for i in range(n - 2, -1, -1):
#             for j1 in range(m):
#                 for j2 in range(m):
#                     ans = float('-inf')

#                     for d1 in range(-1, 2):
#                         for d2 in range(-1, 2):
#                             nj1 = j1 + d1
#                             nj2 = j2 + d2

#                             if 0 <= nj1 < m and 0 <= nj2 < m:
#                                 ans = max(
#                                     ans,
#                                     dp[i + 1][nj1][nj2]
#                                 )

#                     if j1 == j2:
#                         ans += grid[i][j1]
#                     else:
#                         ans += grid[i][j1] + grid[i][j2]

#                     dp[i][j1][j2] = ans

#         return dp[0][0][m - 1]