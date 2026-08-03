class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            curr = 0
            dp[i] = float('-inf')

            for k in range(3):
                if i + k < n:
                    curr += stoneValue[i + k]
                    dp[i] = max(dp[i], curr - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"