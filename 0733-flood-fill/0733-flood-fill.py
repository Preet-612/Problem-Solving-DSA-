class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0]) 
        if image[sr][sc] == color:
            return image
        original = image[sr][sc]
        def dfs(r,c):

            if 0 > r or r >= row or 0 > c or c >= col or image[r][c] != original:
                return
            
            image[r][c] = color
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        
        dfs(sr,sc)
        return image