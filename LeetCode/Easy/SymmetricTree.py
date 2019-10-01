# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
# 1
# / \
#     2   2
# / \ / \
#     3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
# 1
# / \
#     2   2
# \ \
#     3    3



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(l, r):
            if not l and not  r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and isMirror(l.right, r.left) and isMirror(l.left, r.right)

        return isMirror(root, root)