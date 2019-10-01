def maxPathSum(i, j):
    if i == n-1 and j == m-1:
        return grid[i][j]
    if (i, j) in visited:
        print(i, j)
        return visited[(i, j)]
    elif i == n - 1:
        ans = grid[i][j] + maxPathSum(i, j+1)
    elif j == m - 1:
        ans = grid[i][j] + maxPathSum(i+1, j)
    else:
        ans = grid[i][j] + max(maxPathSum(i, j+1), maxPathSum(i+1, j))
    visited[(i, j)] = ans
    return ans


visited = {}
n, m = 4, 4
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(maxPathSum(0, 0))

