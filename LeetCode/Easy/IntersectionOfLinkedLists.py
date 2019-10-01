# Write a program to find the node at which the intersection of two singly linked lists begins.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #     def getIntersectionNode(self, headA, headB):
    #         """
    #         :type head1, head1: ListNode
    #         :rtype: ListNode
    #         """
    #         seen = set()
    #         while headA or headB:
    #             if headA == headB:
    #                 return headA
    #             if headA in seen:
    #                 return headA
    #             elif headB in seen:
    #                 return headB
    #             else:
    #                 if headA:
    #                     seen.add(headA)
    #                     headA = headA.next
    #                 if headB:
    #                     seen.add(headB)
    #                     headB = headB.next

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        if not p or not q:
            return None
        while p != q:
            p, q = p.next, q.next
            if not p:
                if not q:
                    break
                p = headB
            if not q:
                q = headA
        return p