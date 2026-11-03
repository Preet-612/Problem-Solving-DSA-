class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        ans = 0

        for num in nums:
            ans += maxi - num

        return ans