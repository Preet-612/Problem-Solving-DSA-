class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))

        pos = {num: i for i, num in enumerate(nums)}
        vis = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if vis[i] or pos[arr[i]] == i:
                continue

            cycle = 0
            j = i

            while not vis[j]:
                vis[j] = True
                j = pos[arr[j]]
                cycle += 1

            swaps += cycle - 1

        return swaps
