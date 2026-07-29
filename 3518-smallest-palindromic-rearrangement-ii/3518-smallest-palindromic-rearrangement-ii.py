class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        freq = Counter(s)

        mid = ""
        half = {}

        length = 0
        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ch] = freq[ch] // 2
            length += half[ch]

        # nCr with early stopping
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            ans = 1
            for i in range(1, r + 1):
                ans = ans * (n - r + i) // i
                if ans > LIMIT:
                    return LIMIT
            return ans

        # number of permutations for current counts
        def countWays():
            rem = sum(half.values())
            ways = 1
            left = rem

            for ch in sorted(half):
                f = half[ch]
                if f:
                    ways *= comb(left, f)
                    if ways > LIMIT:
                        return LIMIT
                    left -= f
            return ways

        if countWays() < k:
            return ""

        first = []

        while sum(half.values()) > 0:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = countWays()

                if ways >= k:
                    first.append(ch)
                    break
                else:
                    k -= ways
                    half[ch] += 1

        first = "".join(first)
        return first + mid + first[::-1]