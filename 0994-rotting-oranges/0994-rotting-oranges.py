class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minute = 0
        if fresh == 0:
            return 0
        
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:

            size = len(q)

            for i in range(size):

                r, c = q.popleft()

                for cr, cc in direction:
                    nr, nc = cr + r, cc + c

                    if 0 <= nr < row and 0<= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            
            minute += 1

        return minute if fresh == 0 else -1 

