class Solution:
    def rob(self, nums: List[int]) -> int:
# space optimization
        n = len(nums)

        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1
# tabulation

        # n = len(nums)

        # if n == 1:
        #     return nums[0]

        # dp = [0] * n

        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     take = nums[i] + dp[i - 2]
        #     skip = dp[i - 1]

        #     dp[i] = max(take, skip)

        # return dp[n - 1]

# memoization

        # n = len(nums)
        # dp = [-1] * n

        # def solve(i):
        #     if i == 0:
        #         return nums[i]
        #     if i < 0:
        #         return 0

        #     if dp[i] != -1:
        #         return dp[i]

        #     take = nums[i] + solve(i - 2)
        #     skip = solve(i - 1)

        #     dp[i] = max(take, skip)
        #     return dp[i]

        # return solve(n-1)