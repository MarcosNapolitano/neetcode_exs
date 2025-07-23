#!/usr/bin/python3

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> [TreeNode]:

        indexes = {}

        for i in range(len(inorder)):
            indexes[inorder[i]] = i

        def recursive(preorder, inorder):

            print(preorder)
            if not preorder or not inorder:
                return None

            head = TreeNode(preorder[0])
            head.left = recursive(preorder[1:indexes.get(head.val) + 1])
            head.right = recursive(preorder[indexes.get(head.val) + 1:])
            return head

        return recursive(preorder, inorder)


obj = Solution()
print(obj.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
