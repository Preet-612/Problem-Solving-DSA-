class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        less = min(nums)
        more = max(nums)
        res = []
        for i in range(less,more):
            if i not in nums:
                res.append(i)
        
        return res
