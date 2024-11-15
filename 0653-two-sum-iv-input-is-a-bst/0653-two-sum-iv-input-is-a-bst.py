class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(root):
            if not root:
                return False
            if root.val in seen:
                return True
            seen[k-root.val] = 1
            return helper(root.left) or helper(root.right)
        seen = {}
        return helper(root)