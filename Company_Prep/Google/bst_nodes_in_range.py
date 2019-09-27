# Given a Binary Search Tree (BST) and a range l-h(inclusive), count the number of nodes in the BST that lie in the given range.
#
# The values smaller than root go to the left side
# The values greater and equal to the root go to the right side
# Input Format:
# The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of three lines. Description of  test cases is as follows:
# The First line of each test case contains an integer 'N' which denotes the no of nodes in the BST.   .
# The Second line of each test case contains 'N' space separated values of the nodes in the BST.
# The Third line of each test case contains two space separated integers 'l' and 'h' denoting the range, where l < h
#
# Output:
# For each testcase, in a new line, output the number of nodes that lie in the range l-h.
#
# Your Task:
# This is a function problem. You don't have to take input. You are required to complete the function getCountOfNode() that takes root, l ,h as parameters and returns the count.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 1 <= l < h < 103
#
# Example:
# Input:
# 2
# 6
# 10 5 50 1 40 100
# 5 45
# 5
# 5 6 7 4 3
# 2 8
#
# Output:
# 3
# 5


#Initial Template for Python 3
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)

    return root


def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)

        lr=[int(x) for x in input().strip().split()]
        print(getCountOfNode(root,lr[0],lr[1]))
        testcases-=1
if __name__=="__main__":
    main()
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Structure of node
'''
# Node Class:
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
'''
##Complete this function


def getCountOfNode(root,l,h):
    ##Your code here
    if root == None:
        return 0
    if root.data == l and root.data == h:
        return 1
    elif root.data >=l and root.data <= h:
        return 1 + getCountOfNode(root.left, l, h) + getCountOfNode(root.right, l, h)
    elif root.data < l:
        return getCountOfNode(root.right, l, h)
    else:
        return getCountOfNode(root.left, l, h)