#!usr/bin/python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: [TreeNode]) -> bool:

        def dfs(root: TreeNode) -> bool:

            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            if left - right >= 2:
                self.balanced = False

            return 1 + max(left, right)

        dfs(root)
        return self.balanced


# tree playground!

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(4)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g

debug = Solution()

print(debug.isBalanced(a))
