class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def level_order(node):
    if not node:
        return
    q = []
    q.append(node)
    while q:
        print(q[0].data, end=' ')
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end=' ')
        inorder(node.right)


def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

level_order(root)
print()
inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
