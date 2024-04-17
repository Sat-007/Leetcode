# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        
        def helper(root, curS):
            if not root:
                return 
            
            curS = chr(ord("a") + root.val) + curS
            
            if root.left and root.right:
                return min(helper(root.left,curS) , helper(root.right,curS))
                
            if root.left:
                return helper(root.left,curS)
                
                
            if root.right:
                return helper(root.right,curS)
                
            
            
            return curS
        return helper(root,"")