# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def BFS(x, y, grid):
            if x >= len(grid) or x < 0 or y >= len(grid[x]) or y < 0 or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            BFS(x, y+1, grid)
            BFS(x+1, y, grid)
            BFS(x-1, y, grid)
            BFS(x, y-1, grid)
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    BFS(i, j, grid)
        return islands
