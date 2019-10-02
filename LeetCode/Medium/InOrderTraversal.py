# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # def inorderTraversal(self, root):
    #         """
    #         :type root: TreeNode
    #         :rtype: List[int]
    #         """
    #         def inOrder(root):
    #             if root:
    #                 inOrder(root.left)
    #                 ans.append(root.val)
    #                 inOrder(root.right)
    #         ans = []
    #         inOrder(root)
    #         return ans

    # iterative
    def inorderTraversal(self, root):

        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans