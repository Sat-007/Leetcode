from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colZero = False  # Flag to track if the first column should be zeroed

        # Step 1: Mark rows and columns
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                colZero = True  # Mark if the first column should be zeroed

            for c in range(1, len(matrix[0])):  # Start from column 1 to avoid overwriting the first column flag
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # Mark the row
                    matrix[0][c] = 0  # Mark the column

        # Step 2: Set matrix elements to zero based on markers, starting from the bottom-right
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, 0, -1):  # Process all columns except the first one
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            # Handle the first column separately
            if colZero:
                matrix[i][0] = 0
