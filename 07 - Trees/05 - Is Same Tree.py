#!/usr/bin/python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.same = True

    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:

        def test(p: [TreeNode], q: [TreeNode]) -> None:

            if not p and not q or not self.same:
                return

            if not (p and q) or p.val != q.val:
                self.same = False
                return

            test(p.left, q.left)
            test(p.right, q.right)

        test(p, q)
        return self.same


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(1)
e = TreeNode(2)

a.left = b
c.left = None
c.right = e

o = Solution()
print(o.isSameTree(a, c))
