class Solution:
    def shortestPathBinaryMatrix(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sr = sc = 0
        dr = dc = n-1


        if mat[sr][sc] == 1 or mat[dr][dc] == 1:
            return -1
        infi = float('inf')
        dist = [[infi]*n for i in range(n)]

        dist[sr][sc] = 1

        q = deque([(sr,sc)])

        while q:

            r,c = q.popleft()
            if (r,c) == (dr,dc):
                return dist[r][c]

            for i, j in [(-1,-1),(-1,1),(1,-1),(0,1),(0,-1),(1,0),(-1,0),(1,1)]:

                nr, nc = r+i, c+j

                if 0 <= nr < n and 0 <= nc < n and mat[nr][nc] == 0:
                    if dist[r][c] + 1 < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr,nc))

        return -1
