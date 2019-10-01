# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):

        slow = fast = head
        prev_node = None
        while fast and fast.next:
            fast = fast.next.next
            head = head.next

            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        if fast:
            head = head.next
        while prev_node and head:
            if prev_node.val!=head.val:
                return False

            prev_node = prev_node.next
            head = head.next

        return True