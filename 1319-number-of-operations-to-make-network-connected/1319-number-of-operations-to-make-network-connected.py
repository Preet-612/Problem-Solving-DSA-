class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return -1

        dsu = DSU(n)

        for u, v in connections:
            dsu.union(u, v)

        components = 0
        for i in range(n):
            if dsu.find(i) == i:
                components += 1

        return components - 1