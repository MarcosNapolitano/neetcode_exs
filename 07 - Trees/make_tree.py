#!/usr/bin/python3

from collections import deque


class TreeNode:
    def __init__(self,  val=0,  left=None,  right=None):
        self.val = val
        self.left = left
        self.right = right


def makeTree(arr):

    arr.reverse()
    head = TreeNode(arr.pop())
    queue = deque()
    queue.appendleft(head)

    while queue:

        if not arr:
            queue.pop()
            break

        node_left = arr.pop()
        node_right = arr.pop()
        current_element = queue.pop()

        if node_left is not None:
            current_element.left = TreeNode(node_left)
            queue.appendleft(current_element.left)

        if node_right is not None:
            current_element.right = TreeNode(node_right)
            queue.appendleft(current_element.right)

    return head


tree = makeTree([-5, -1, -4, None, None, -5, 0, -5, None, -1, 2,
                 None, None, None, -3, None, None, None, -5, None, -4])
