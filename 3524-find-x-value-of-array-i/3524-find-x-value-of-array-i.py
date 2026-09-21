class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at previous index
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            value = num % k

            # Start a new subarray with only num
            new_dp[value] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * value) % k
                    new_dp[new_remainder] += dp[r]

            # Add all subarrays ending at current position
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result