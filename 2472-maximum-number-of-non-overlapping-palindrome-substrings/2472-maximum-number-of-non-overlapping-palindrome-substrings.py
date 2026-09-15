class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[l][r] = True if s[l:r+1] is palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for r in range(n):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 1 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        # dp[i] = maximum number of palindromes
        # using first i characters
        dp = [0] * (n + 1)

        for r in range(n):
            # Don't select a palindrome ending at r
            dp[r + 1] = dp[r]

            for l in range(r + 1):
                length = r - l + 1

                if length >= k and pal[l][r]:
                    dp[r + 1] = max(dp[r + 1], dp[l] + 1)

        return dp[n]