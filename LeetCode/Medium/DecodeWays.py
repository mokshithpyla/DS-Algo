# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def find_ways(string, start, end):
            if start in decoded:
                return decoded[start]
            if start < end and string[start] == '0':
                return 0
            if start >= end:
                return 1
            total = find_ways(string, start + 1, end)
            s = string[start:start+2]
            if len(s) == 2 and int(s) <= 26:
                total += find_ways(string, start + 2, end)
            decoded[start] = total
            return decoded[start]
        decoded = {}
        return find_ways(s, 0, len(s))


# class Solution:
#     def numDecodings(self, s):
#         if not s or s[0] == '0':
#             return 0
#         n = len(s)
#         if n == 1:
#             return 1

#         dp = [0] * (n + 1)
#         dp[0] = 1
#         dp[1] = 1

#         for i in range(2, n + 1):
#             one = int(s[i-1])
#             two = int(s[i-2 : i])

#             if 1 <= one <= 9:
#                 dp[i] += dp[i-1]

#             if 10 <= two <= 26:
#                 dp[i] += dp[i-2]

#         return dp[n]