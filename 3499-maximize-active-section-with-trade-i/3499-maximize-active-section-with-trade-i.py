class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        ans = total_ones

        # Augmented string
        t = "1" + s + "1"

        # Run-length encoding
        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        # Check every 0-1-0 pattern
        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == '1'
                and runs[i - 1][0] == '0'
                and runs[i + 1][0] == '0'
            ):
                ans = max(ans, total_ones + runs[i - 1][1] + runs[i + 1][1])

        return ans