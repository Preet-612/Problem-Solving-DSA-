class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0
        non_zero = False

        for num in nums:
            x ^= num
            if num != 0:
                non_zero = True

        if x != 0:
            return len(nums)

        return len(nums) - 1 if non_zero else 0