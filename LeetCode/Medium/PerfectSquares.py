# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def find(squares, total):
            if total < 0:
                return -1
            if total == 0:
                return 0
            if total in count:
                return count[total]
            else:
                min_squares = total
                res = 0
                for square in squares:
                    res = find(squares, total - square)
                    if res >=0 and res < min_squares:
                        min_squares = 1 + res
                count[total] = min_squares
                return count[total]
        k = n**0.5
        if int(k)**2 == n:
            return 1
        else:
            count = {}
            k = int(k)
            dp = [i for i in range(0, n+1)]

            squares = [i*i for i in range(1, k+1)]
            return find(squares, n)

#             ans = float('inf')
#             for square in squares:
#                 for i in range(square, n+1):
#                     if i >= square:
#                         dp[i] = min(dp[i], 1 + dp[i-square])
#                 ans = min(ans, dp[i])
#             return ans