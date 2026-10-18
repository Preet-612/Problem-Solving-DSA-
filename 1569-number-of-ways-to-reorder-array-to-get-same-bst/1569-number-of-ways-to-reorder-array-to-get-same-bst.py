class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * (n + 1)
        invfact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def comb(n, r):
            return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            l = len(left)
            r = len(right)

            ways = comb(l + r, l)
            ways = ways * solve(left) % MOD
            ways = ways * solve(right) % MOD

            return ways

        return (solve(nums) - 1) % MOD
