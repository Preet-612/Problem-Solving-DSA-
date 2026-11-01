class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        moves = 0

        for num in nums:
            moves += num - mini

        return moves