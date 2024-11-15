# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        
        def in_order(root, values):
            if root:
                in_order(root.left, values)
                values.append(root.val)
                in_order(root.right, values)
                
        values = []
        in_order(root, values)        
            
        l = 0 
        r = len(values) - 1

        while l < r:
            summ = values[l] + values[r]
            if summ == k:
                return True
            elif summ < k:
                l += 1
            else:
                r -= 1
        return False

       