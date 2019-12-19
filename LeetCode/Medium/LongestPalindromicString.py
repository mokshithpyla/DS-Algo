# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ''
        for i in range(len(s)):
            longestSoFar = findPalindrome(i, i)
            ans = longestSoFar if len(longestSoFar) > len(ans) else ans
            longestSoFar = findPalindrome(i, i+1)
            ans = longestSoFar if len(longestSoFar) > len(ans) else ans
        return ans

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ''
#         for center in range(2*len(s)):
#             left = center // 2
#             right = left + center % 2
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 palindrome = s[left:right+1]
#                 left -= 1
#                 right += 1
#             ans = palindrome if len(palindrome) > len(ans) else ans
#         return ans
