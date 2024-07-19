class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #     0   1    2
        #
        # 0   3    7    8 
        # 1   9    11   13
        # 2   15   16   17
        
        
        
        ROWS = len (matrix)
        COLS = len(matrix[0])
        maxof = float('-inf')
        for r in range(ROWS):
            row_min = min(matrix[r])
            maxof = max(row_min,maxof)
            
        for c in range(COLS):
            col_max = matrix[0][c]
            
            for r in range(ROWS):
                col_max = max(col_max, matrix[r][c])
            
            
            if col_max == maxof:
                return [col_max] 
        
    