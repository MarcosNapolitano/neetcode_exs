#!/usr/bin/python3
from make_tree import makeTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        global good_nodes
        good_nodes = 0

        def df(root: TreeNode, current_max=None) -> int:

            global good_nodes

            if not root:
                return None

            if current_max is None or root.val >= current_max:
                good_nodes += 1
                current_max = root.val

            df(root.left, current_max)
            df(root.right, current_max)

            return root.val

        df(root)
        return good_nodes


tree = makeTree([-5, -1, -4, None, None, -5, 0, -5, None, -1, 2, None, None,
                None, -3, None, None, None, -5, None, -4])

obj = Solution()
print(obj.goodNodes(tree))
