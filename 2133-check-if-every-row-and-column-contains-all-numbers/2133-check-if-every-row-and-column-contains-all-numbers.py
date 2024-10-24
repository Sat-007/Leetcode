class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            row_check = [False] * n
            col_check = [False] * n 
            for j in range(n):
                row = matrix[i][j]
                if row < 0 or row > n or row_check[row-1]:
                    return False
                row_check[row - 1] = True
                col = matrix[j][i]
                if col < 0 or col > n or col_check[col-1]:
                    return False
                col_check[col - 1] = True
        return True
                