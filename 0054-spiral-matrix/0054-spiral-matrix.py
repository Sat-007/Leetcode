class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])
        result=[]
        while top<bottom and left<right:
            
            result+=matrix[top][left:right]
            top+=1
           
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right-=1
            if not (left < right and top < bottom):
                break
            
            result+=matrix[bottom-1][left:right][::-1]
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left+=1
        return result
        
        
            
        