# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        head = temp = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                s = c + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            else:
                if l1:
                    s = c + l1.val
                    l1 = l1.next
                else:
                    s = c + l2.val
                    l2 = l2.next
            c = s/10
            s = s%10
            temp.next = ListNode(s)
            temp = temp.next
        if c == 1:
            temp.next = ListNode(1)

        return head.next