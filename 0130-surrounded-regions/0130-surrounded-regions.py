class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        visited = [[False]*col for i in range(row)]



        def dfs(r,c):
            if 0 > r or 0 > c or r >= row or c >= col or visited[r][c] == True or board[r][c] == "X":
                return 
            visited[r][c] = True
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)





        for i in range(col):
            if not visited[0][i] and board[0][i] == "O":
                dfs(0,i)

            if not visited[row-1][i] and board[row-1][i] == "O":
                dfs(row-1,i)
        
        for i in range(row):
            if not visited[i][0] and board[i][0] == "O":
                dfs(i,0)

            if not visited[i][col-1] and board[i][col-1] == "O":
                dfs(i,col-1)
        
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and board[i][j] == "O":
                    board[i][j] = "X"


