class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # exact[g] = number of pairs with gcd exactly g
        exact = [0] * (mx + 1)

        # Compute from large to small
        for g in range(mx, 0, -1):
            cnt = 0
            for multiple in range(g, mx + 1, g):
                cnt += freq[multiple]

            pairs = cnt * (cnt - 1) // 2
            exact[g] = pairs

            for multiple in range(2 * g, mx + 1, g):
                exact[g] -= exact[multiple]

        # Prefix counts
        prefix = []
        gcds = []

        running = 0
        for g in range(1, mx + 1):
            if exact[g]:
                running += exact[g]
                prefix.append(running)
                gcds.append(g)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcds[idx])

        return ans