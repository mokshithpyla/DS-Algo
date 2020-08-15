# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
# 
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ans = True
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if stack:
                    top = stack.pop()
                else:
                    ans = False
                    break
                if top == '(' and s[i] in [']','}']:
                    ans = False
                    break
                elif top =='[' and s[i] in [')','}']:
                    ans = False
                    break
                elif top =='{' and s[i] in [')',']']:
                    ans = False
                    break
        if len(stack):
            ans = False
        return ans