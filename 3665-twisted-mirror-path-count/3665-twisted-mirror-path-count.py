class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [0] * n

        for i in range(m):
            left = 0

            for j in range(n):

                if i == 0 and j == 0:
                    ways = 1

                else:
                    top = dp[j]
                    dp[j] = 0

                    if grid[i][j] == 1:
                        # Mirror:
                        # From left -> down
                        # From top -> right

                        dp[j] = left
                        left = top

                        continue

                    ways = left + top

                    if ways >= MOD:
                        ways -= MOD

                if i == m - 1 and j == n - 1:
                    return ways

                # Empty cell: move right and down
                dp[j] = ways
                left = ways

        return 0