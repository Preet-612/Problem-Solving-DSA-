class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        
        infi = float('inf')
        dist = [[infi]*n for i in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for via in range(n):
            temp = False
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != infi and dist[via][j] != infi:
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
                        temp = True
            if not temp:
                break


        minnum = n
        res = -1
        for i in range(n):
            count = 0

            for j in range(n):

                if dist[i][j] <= distanceThreshold:
                    count += 1
            count -= 1
            if count <= minnum:
                minnum = count
                res = i
        
        return res











