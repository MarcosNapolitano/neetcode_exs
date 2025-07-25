# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return "Not Found"

        if not p:
            return q

        if not q or p.val == root.val:
            return p

        if q.val == root.val:
            return q

        if min(p.val, q.val) < root.val < max(p.val, q.val):
            return root

        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root
