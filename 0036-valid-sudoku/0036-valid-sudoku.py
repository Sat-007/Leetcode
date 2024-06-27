class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num !=".":
                    if (num,i) in seen:
                        return False
                    seen.add((num,i))
                    
                    if (j,num) in seen:
                        return False
                    seen.add((j,num))
                    
                    box = (i // 3, j // 3)
                    if (box,num) in seen:
                        return False
                    seen.add((box,num))
                    #print(seen)
        return True
                    