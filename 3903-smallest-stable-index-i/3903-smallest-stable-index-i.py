class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            temp = max(nums[0:i+1]) - min(nums[i:n])
            if temp <= k:
                return i

        
        return -1