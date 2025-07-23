#!/usr/bin/python3

from make_tree import makeTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: [TreeNode]) -> list[list[int]]:

        if not root:
            return []

        result = [root.val]
        stack = []
        queue = [root]

        while queue:

            stack = []

            for i in range(len(queue)):

                current_element = queue.pop(0)

                if current_element:

                    if current_element.right:
                        stack.append(current_element.right.val)
                    else:
                        if current_element.left:
                            stack.append(current_element.left.val)

                    queue.append(current_element.left)
                    queue.append(current_element.right)

            if stack:
                result.append(stack.pop())

        return result


tree = makeTree([1, None, 2])
obj = Solution()
print(obj.rightSideView(tree))
