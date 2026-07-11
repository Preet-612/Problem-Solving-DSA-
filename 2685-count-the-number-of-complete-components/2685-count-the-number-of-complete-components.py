class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True

            nodes = 1
            edgeCount = len(adj[node])

            for nei in adj[node]:
                if not visited[nei]:
                    n1, e1 = dfs(nei)
                    nodes += n1
                    edgeCount += e1

            return nodes, edgeCount

        for i in range(n):
            if not visited[i]:
                nodes, edgeCount = dfs(i)

                actualEdges = edgeCount // 2
                requiredEdges = nodes * (nodes - 1) // 2

                if actualEdges == requiredEdges:
                    ans += 1

        return ans