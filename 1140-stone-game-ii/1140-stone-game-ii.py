class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, M):
            if i >= n:
                return 0

            if dp[i][M] != -1:
                return dp[i][M]

            ans = 0

            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                taken = suffix[i] - suffix[i + X]

                opponent = dfs(i + X, max(M, X))

                ans = max(ans, taken + (suffix[i + X] - opponent))

            dp[i][M] = ans
            return ans

        return dfs(0, 1)