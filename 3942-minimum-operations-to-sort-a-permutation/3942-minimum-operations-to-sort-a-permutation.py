from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        inc = all(
            nums[(i + 1) % n] == (nums[i] + 1) % n
            for i in range(n)
        )

        dec = all(
            nums[(i + 1) % n] == (nums[i] - 1) % n
            for i in range(n)
        )

        ans = float('inf')

        if inc:
            k = nums[0]
            if k == 0:
                return 0
            ans = min(ans, n - k, k + 2)

        if dec:
            k = (n - 1 - nums[0]) % n
            ans = min(ans, min(k, n - k) + 1)

        return ans if ans != float('inf') else -1