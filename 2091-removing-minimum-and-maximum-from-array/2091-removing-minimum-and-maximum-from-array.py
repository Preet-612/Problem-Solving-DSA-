class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        front = right + 1
        back = n - left
        both = min(left + 1 + n - right,
                   right + 1 + n - left)

        return min(front, back, both)