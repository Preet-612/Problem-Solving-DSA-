class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return []
        
        nums.sort()
        
        temp = []
        for i,j in enumerate(nums):
            if j == target:
                temp.append(i)
        
        return temp