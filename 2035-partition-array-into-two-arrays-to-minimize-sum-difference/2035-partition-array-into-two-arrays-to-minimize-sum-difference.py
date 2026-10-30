from typing import List
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)

        left = [[] for _ in range(n + 1)]
        right = [[] for _ in range(n + 1)]

        for mask in range(1 << n):
            s1 = 0
            s2 = 0
            cnt = 0

            for i in range(n):
                if mask & (1 << i):
                    s1 += nums[i]
                    cnt += 1
                else:
                    s2 += nums[n + i]

            left[cnt].append(s1)
            right[n - cnt].append(s2)

        for i in range(n + 1):
            right[i].sort()

        ans = float('inf')

        for k in range(n + 1):
            for s in left[k]:
                target = total / 2 - s

                idx = bisect_left(right[n - k], target)

                if idx < len(right[n - k]):
                    curr = s + right[n - k][idx]
                    ans = min(ans, abs(total - 2 * curr))

                if idx > 0:
                    curr = s + right[n - k][idx - 1]
                    ans = min(ans, abs(total - 2 * curr))

        return ans