class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        nums.sort()
        dp = [1] * n
        parent = [i for i in range(n)]

        maxi = 1
        last = 0

        for i in range(n):
            for prev in range(i):
                if (nums[prev] % nums[i] == 0 or nums[i] % nums[prev] == 0) and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    parent[i] = prev

            if dp[i] > maxi:
                maxi = dp[i]
                last = i

        ans = []

        while parent[last] != last:
            ans.append(nums[last])
            last = parent[last]

        ans.append(nums[last])

        ans.reverse()

        return ans
