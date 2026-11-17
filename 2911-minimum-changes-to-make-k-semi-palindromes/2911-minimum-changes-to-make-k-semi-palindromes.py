
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        # Precompute minimum changes for every substring
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                ans = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for r in range(d):
                        left = i + r
                        right = j - ((j - (i + r)) % d)

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    ans = min(ans, changes)

                cost[i][j] = ans

        # Partition DP
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(2, n + 1):
            for j in range(1, min(k, i // 2) + 1):
                for t in range(2 * (j - 1), i - 1):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[t][j - 1] + cost[t][i - 1]
                    )

        return dp[n][k]
