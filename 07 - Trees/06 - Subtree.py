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

    def sameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:

        def test(p: [TreeNode], q: [TreeNode]) -> None:

            if not p and not q or not self.same:
                return self.same

            if not p or not q or p.val != q.val:
                self.same = False
                return self.same

            else:
                test(p.left, q.left)
                test(p.right, q.right)
                return self.same

        test(p, q)

        return self.same

    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:

        self.same = True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


obj = Solution()

a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)
f = TreeNode(0)

a.left = b
a.right = c
b.left = d
b.right = e

g = TreeNode(4)
h = TreeNode(1)
i = TreeNode(2)
j = TreeNode(1)

g.left = h
g.right = i
h.left = j

print(obj.isSubtree(a, g))
