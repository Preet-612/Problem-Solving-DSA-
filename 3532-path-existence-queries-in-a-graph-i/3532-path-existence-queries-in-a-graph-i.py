class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n
        curr = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr += 1
            comp[i] = curr

        # Answer queries
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans