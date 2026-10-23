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
            return ans

        return helper(0, 0, m - 1)