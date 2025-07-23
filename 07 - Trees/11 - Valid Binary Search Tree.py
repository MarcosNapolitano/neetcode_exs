#!/usr/bin/python3
from make_tree import makeTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def df(root: TreeNode, left: int = -9999999,
               right: int = 9999999) -> int or None:

            if not root:
                return True

            if not (root.val < right and root.val > left):
                return False

            return (df(root.left, left, root.val) and
                    df(root.right, root.val, right))

        return df(root)


tree = makeTree([120, 70, 140, 50, 100, 130, 160, 20, 55, 75, 110, 119, 135, 150, 200])

obj = Solution()
print(obj.isValidBST(tree))
