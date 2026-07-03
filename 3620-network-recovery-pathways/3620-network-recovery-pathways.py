class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        maxCost = 0
        indegree = [0] * n
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            maxCost = max(maxCost, w)

        # Topological order (same for every binary search iteration)
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = 10 ** 18

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    # Intermediate nodes must be online
                    if v != n - 1 and not online[v]:
                        continue

                    dist[v] = min(dist[v], dist[u] + w)

            return dist[n - 1] <= k

        if not check(0):
            return -1

        lo, hi = 0, maxCost
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans