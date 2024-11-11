# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)
            
            curr_sum = l + r + root.val
            
            ans = max(ans, curr_sum)
        
            
            return root.val + max(l,r)
        
        dfs(root)
        return ans
        