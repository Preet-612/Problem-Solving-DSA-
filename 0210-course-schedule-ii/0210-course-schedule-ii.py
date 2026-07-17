class Solution:
    def findOrder(self, V: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * V
        adj = [[] for i in range(V)]
        for u,v in prerequisites:
            adj[v].append(u)

        # Calculate indegree
        for node in range(V):
            for nei in adj[node]:
                indegree[nei] += 1

        q = deque()

        # Push all nodes with indegree 0
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return topo if len(topo) == V else []
        