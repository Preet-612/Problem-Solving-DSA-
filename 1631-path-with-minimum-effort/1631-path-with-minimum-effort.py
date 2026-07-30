import heapq
class Solution:
    def minimumEffortPath(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        sr = sc = 0
        dr = n-1
        dc = m-1

        infi = float('inf')
        dist = [[infi] * m for i in range(n)]
        dist[sr][sc] = 0

        pq = [(0,sr,sc)]

        while pq:
            eff,r,c = heapq.heappop(pq)

            if (r,c) == (dr,dc):
                return eff

            if eff > dist[r][c]:
                continue
            
            for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:

                nr, nc = r+i, c+j

                if 0 <= nr < n and 0 <= nc < m:
                    neweff = max(eff,abs(mat[r][c] - mat[nr][nc]))

                    if neweff < dist[nr][nc]:
                        dist[nr][nc] = neweff
                        heapq.heappush(pq,(neweff,nr,nc))
        return 0


