class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        colZero = False
        
        for r in range(len(matrix)):
             if matrix[r][0] == 0:
                    colZero = True
                    
             for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 
                    matrix[0][c] = 0
            
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, 0 , -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
            if colZero:
                matrix[i][0] = 0  
             