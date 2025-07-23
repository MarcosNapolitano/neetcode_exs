# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:

        curr_max = [0]

        def recursive(root):
            if not root:
                return -1

            left = recursive(root.left)
            right = recursive(root.right)

            curr_max[0] = max(curr_max[0], 2 + left + right)
            return 1 + max(left, right)

        recursive(root)
        return curr_max[0]
