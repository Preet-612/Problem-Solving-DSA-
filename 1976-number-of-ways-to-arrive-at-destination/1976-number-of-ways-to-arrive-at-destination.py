import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj = defaultdict(list)
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        infi = float('inf')
        ways = [0]*n
        dist = [infi]*n
        dist[0] = 0
        ways[0] = 1
        pq = [(0,0)]

        while pq:

            time,node = heapq.heappop(pq)

            if time > dist[node]:
                continue
            
            for nei,t in adj[node]:
                
                if dist[node]+t < dist[nei]:
                    dist[nei] = dist[node] + t
                    ways[nei] = ways[node]
                    heapq.heappush(pq,(dist[nei],nei))
                elif dist[nei] == dist[node]+t:
                    ways[nei] = (ways[nei] + ways[node]) % mod
        
        return ways[n-1]
                 


































