class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):

            # Normal alphabet position
            pos = ord(ch) - ord('a') + 1

            # Reverse alphabet position
            reverse_pos = 27 - pos

            # i is 0-based, so use i + 1
            ans += reverse_pos * (i + 1)

        return ans