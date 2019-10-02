# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Recursive

        # def go(i, j, m, n, visited):
        #     if i == n - 1 and j == m - 1:
        #         return 1
        #     if i > n-1 or j > m-1:
        #         return 0
        #     ways = 0
        #     if (i, j) in visited:
        #         return visited[(i, j)]
        #     else:
        #         visited[(i, j)] = go(i,j+1, m, n, visited) + go(i+1, j, m, n, visited)
        #         return visited[(i, j)]
        # return go(0, 0, m, n, {})

        # Iterative

        dp = [[1]*n]*m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]