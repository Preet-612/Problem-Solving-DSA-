class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return

            grid[r][c] = 0
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for i in range(col):
            if grid[0][i] == 1:
                dfs(0, i)
            if grid[row - 1][i] == 1:
                dfs(row - 1, i)

        for i in range(row):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][col - 1] == 1:
                dfs(i, col - 1)
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    ans += 1

        return ans
