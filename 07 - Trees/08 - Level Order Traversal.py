# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: [TreeNode]) -> list[list[int]]:

        result = []
        current = []
        queue = []
        traverse = [root]

        while queue or traverse:

            current_element = traverse.pop(0)

            if current_element is None:
                continue

            current.append(current_element.val)

            if current_element.left:
                queue.append(current_element.left)
            if current_element.right:
                queue.append(current_element.right)

            if not traverse:
                result.append(current)
                current = []
                while len(queue) != 0:
                    traverse.append(queue.pop(0))

        return result
