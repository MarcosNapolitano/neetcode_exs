#!/usr/bin/python3
from make_tree import makeTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:

        global currentMin
        global tries

        currentMin = root.val
        tries = k

        def df(root):

            global currentMin
            global tries

            if not root:
                return None

            df(root.left)

            if tries > 0:
                currentMin = root.val
                tries -= 1

            df(root.right)

        df(root)
        return currentMin


tree = makeTree([3, 1, 4, None, 2])

obj = Solution()
print(obj.kthSmallest(tree, 3))  # el problema es que siempre compara al minimo, no al segundo minimo
