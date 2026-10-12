class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
       
        MOD = 10**9 + 7
        cnt = [0] * 32

        for num in nums:
            for b in range(32):
                if num & (1 << b):
                    cnt[b] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for b in range(32):
                if cnt[b] > 0:
                    num |= (1 << b)
                    cnt[b] -= 1

            ans = (ans + num * num) % MOD

        return ans