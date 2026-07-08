class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix numbers
        prefNum = [0] * (k + 1)
        for i in range(k):
            prefNum[i + 1] = (prefNum[i] * 10 + digits[i]) % MOD

        # prefix digit sums
        prefSum = [0] * (k + 1)
        for i in range(k):
            prefSum[i + 1] = prefSum[i] + digits[i]

        ans = []

        for L, R in queries:
            l = bisect_left(pos, L)
            r = bisect_right(pos, R) - 1

            if l > r:
                ans.append(0)
                continue

            length = r - l + 1

            x = (prefNum[r + 1] - prefNum[l] * pow10[length]) % MOD
            digit_sum = prefSum[r + 1] - prefSum[l]

            ans.append((x * digit_sum) % MOD)

        return ans