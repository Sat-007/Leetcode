# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        count = 0  
        def dfs(node, ps):
            nonlocal count
            if not node:
                return 
            
            
            cs = ps + node.val
            
            x = cs - targetSum
            
            if x in freq:
                count += freq[x]
            
            if cs in freq:
                freq[cs] += 1
                
            else:
                freq[cs] = 1
            
            dfs(node.left, cs)
            dfs(node.right, cs)
            freq[cs] -= 1
            
                
       
        freq = {0: 1}  
        dfs(root, 0)
        return count