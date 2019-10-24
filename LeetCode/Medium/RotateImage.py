# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#
# Given input matrix =
# [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#     [7,4,1],
#     [8,5,2],
#     [9,6,3]
# ]


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i = 0
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i, j) not in visited:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    visited.add((i,j))
                    visited.add((j, i))
        i = 0
        for each in matrix:
            matrix[i] = each[::-1]
            i += 1