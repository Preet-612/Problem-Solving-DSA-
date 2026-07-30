class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        adj = [[] for i in range(n)]

        for u,v,cost in flights:
            adj[u].append((v,cost))
        
        infi = float('inf')
        dist = [infi]*n

        dist[src] = 0
        q = deque([(src,0)])
        stop = 0
        while q and stop <= k:
            temp = dist[:]

            for i in range(len(q)):
                node,cost = q.popleft()

                for nei,price in adj[node]:

                    if cost+price < temp[nei]:
                        temp[nei] = cost + price
                        q.append((nei,temp[nei]))
            
            dist = temp
            stop += 1
        
        return -1 if dist[dst] == infi else dist[dst]























