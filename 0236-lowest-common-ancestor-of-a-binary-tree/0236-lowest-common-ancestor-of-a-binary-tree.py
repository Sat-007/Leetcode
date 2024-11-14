class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', n1: 'TreeNode', n2: 'TreeNode') -> 'TreeNode':
        # Base Case
        if root is None:
            return None

        # If either n1 or n2 matches with root's key, return root
        if root == n1 or root == n2:
            return root

        # Look for LCA in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, n1, n2)
        right_lca = self.lowestCommonAncestor(root.right, n1, n2)

        # If both left and right are non-null, root is LCA
        if left_lca and right_lca:
            return root

        # If only one subtree has a non-null result, return it
        return left_lca if left_lca is not None else right_lca
