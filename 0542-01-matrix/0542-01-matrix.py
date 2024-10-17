class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        q = []
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                    
                else:
                    mat[r][c] = "#"
                    
        check = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for row, col in q:
            for dx, dy in check:
                nr = row + dx
                nc = col + dy
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[row][col] + 1
                    q.append((nr,nc))
                    
        return mat
                    
                    