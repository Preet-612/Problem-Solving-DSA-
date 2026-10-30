import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            d, u, cnt = heapq.heappop(pq)

            if d != dist[u][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in adj[u]:
                if labels[u] == labels[v]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_dist = d + w

                if new_dist < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_dist
                    heapq.heappush(pq, (new_dist, v, new_cnt))

        return -1