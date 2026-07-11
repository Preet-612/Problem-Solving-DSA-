class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row = len(mat)
        col = len(mat[0])

        q = deque()
        dist = [[-1]*col for i in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                    dist[i][j] = 0
        
        while q:

            r, c = q.popleft()

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = dr+r , dc+c

                if 0 <= nr < row and 0 <= nc < col and dist[nr][nc] == -1:

                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr,nc))
        
        return dist
