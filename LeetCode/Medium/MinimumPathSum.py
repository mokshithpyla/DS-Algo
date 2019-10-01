# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def go(i,j):
            if (i, j) in visited:
                return visited[(i, j)]
            if i == n-1 and j == m-1:
                return grid[i][j]
            elif i == n-1:
                return grid[i][j] + go(i, j+1)
            elif j == m-1:
                return grid[i][j] + go(i+1, j)
            else:
                ans = grid[i][j] + min(go(i, j+1), go(i+1, j))
                visited[(i, j)] = ans
            return ans
        visited = {}
        n = len(grid)
        m = len(grid[0])
        return go(0, 0)