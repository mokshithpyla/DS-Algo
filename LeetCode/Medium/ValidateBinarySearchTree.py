# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        stack.append((root, float('-inf'), float('inf')))
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            if root.val <= lower or root.val >= upper:
                return False
            stack.append((root.right, root.val, upper))
            stack.append((root.left, lower, root.val))
        return True