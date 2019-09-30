# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made.
#
# It is guaranteed that the answer is unique.
#
#
#
# Example 1:
#
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:
#
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:
#
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt = []
        for each in s:
            if cnt and cnt[-1][0] == each:
                cnt[-1][1] += 1
                if cnt[-1][1] == k:
                    cnt.pop()
            else:
                cnt.append([each, 1])
        ans = ''
        for c,f in cnt:
            ans += c*f
        return ans