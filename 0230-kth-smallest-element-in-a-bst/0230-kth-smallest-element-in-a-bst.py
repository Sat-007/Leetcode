# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.k = k 
        def InOrder(root):
            
            if root is None or self.result is not None:
                return
            InOrder(root.left)
            self.k -= 1
            if self.k == 0 :
                self.result = root.val
                return
            InOrder(root.right)
        InOrder(root)
        return self.result
        
        