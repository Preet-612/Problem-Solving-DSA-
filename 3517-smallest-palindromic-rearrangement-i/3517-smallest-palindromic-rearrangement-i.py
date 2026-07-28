class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        first_half = []
        middle = ""

        for i in range(26):
            first_half.append(chr(i + ord('a')) * (freq[i] // 2))
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))

        first_half = "".join(first_half)
        second_half = first_half[::-1]

        return first_half + middle + second_half