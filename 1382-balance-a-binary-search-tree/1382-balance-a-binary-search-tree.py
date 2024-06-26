# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        print(res)
        
        def build(l,r):
            if l > r:
                return None
            m = (l+r) // 2
            return TreeNode(res[m], build(l,m-1), build(m + 1, r ))
        return build(0, len(res) - 1)