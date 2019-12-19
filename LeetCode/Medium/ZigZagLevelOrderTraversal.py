# https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1

''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def zigZagTraversal(root):
    '''
    param: root:   root of tree
    return None, no need to print new line
    '''

    q = []
    q.append(root)
    changeDirection = False
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if changeDirection:
            changeDirection = False
            for each in level[::-1]:
                print(each, end=' ')
        else:
            changeDirection = True
            for each in level:
                print(each, end=' ')
