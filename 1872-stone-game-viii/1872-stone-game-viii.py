class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = sum(stones)
        ans = prefix

        for i in range(len(stones) - 2, 0, -1):
            prefix -= stones[i + 1]
            ans = max(ans, prefix - ans)

        return ans