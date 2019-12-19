# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    # code here
    q = []
    q.append(root)
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(level[0], end=' ')