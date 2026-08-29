class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        pairs = sorted((nums[i], i) for i in range(n))
        
        ans = nums[:]
        start = 0
        
        for i in range(1, n + 1):
            if i == n or pairs[i][0] - pairs[i - 1][0] > limit:
                values = [pairs[j][0] for j in range(start, i)]
                indices = sorted(pairs[j][1] for j in range(start, i))
                
                for idx, val in zip(indices, values):
                    ans[idx] = val
                
                start = i
        
        return ans