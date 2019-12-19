''' This is a function problem.You only need to complete the function given below '''
"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def reverse(head, k):
    # Code here
    tails = []
    heads = []
    i = 0
    while head:
        if not head:
            break
        prev = None
        curr = head
        tails.append(curr)
        new = None
        for i in range(k):
            if curr:
                new = curr.next
                curr.next = prev
                prev = curr
                curr = new
        heads.append(prev)
        head = new
        i += 1
    for i in range(len(tails)-1):
        tails[i].next = heads[i+1]
    tails[-1].next = None
    return heads[0]