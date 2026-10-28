
        
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                curr = set()

                if i > 0:
                    for x in dp[j]:
                        curr.add(x ^ grid[i][j])

                if j > 0:
                    for x in dp[j - 1]:
                        curr.add(x ^ grid[i][j])

                dp[j] = curr

        return min(dp[n - 1])