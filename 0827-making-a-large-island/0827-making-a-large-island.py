class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.size[pu] += self.size[pv]


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)

        def node(r, c):
            return r * n + c

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    if r + 1 < n and grid[r + 1][c] == 1:
                        dsu.union(node(r, c), node(r + 1, c))

                    if c + 1 < n and grid[r][c + 1] == 1:
                        dsu.union(node(r, c), node(r, c + 1))

        ans = 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    root = dsu.find(node(r, c))
                    ans = max(ans, dsu.size[root])

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    curr = 1

                    for nr, nc in [
                        (r - 1, c),
                        (r + 1, c),
                        (r, c - 1),
                        (r, c + 1)
                    ]:
                        if 0 <= nr < n and 0 <= nc < n:
                            if grid[nr][nc] == 1:
                                root = dsu.find(node(nr, nc))

                                if root not in seen:
                                    seen.add(root)
                                    curr += dsu.size[root]

                    ans = max(ans, curr)

        return ans