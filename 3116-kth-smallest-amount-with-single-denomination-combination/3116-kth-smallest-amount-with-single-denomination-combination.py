from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins, k):
        coins.sort()
        arr = []

        for coin in coins:
            if not any(coin % x == 0 for x in arr):
                arr.append(coin)

        subsets = []

        def lcm(a, b):
            return a // gcd(a, b) * b

        n = len(arr)

        for mask in range(1, 1 << n):
            cur_lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    cur_lcm = lcm(cur_lcm, arr[i])
                    bits += 1

            if cur_lcm <= 10**18:
                subsets.append((cur_lcm, 1 if bits % 2 else -1))

        def count(x):
            total = 0
            for value, sign in subsets:
                total += sign * (x // value)
            return total

        left, right = 1, min(arr) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left