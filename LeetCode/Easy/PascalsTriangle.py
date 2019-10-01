# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#     [1],
#     [1,1],
#     [1,2,1],
#     [1,3,3,1],
#     [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return None
        if numRows == 1:
            return [[1]]
        ans = [[1],[1,1]]
        for i in range(2,numRows):
            row = [1]
            for j in range(0, len(ans[-1])-1):
                s = ans[-1][j]+ans[-1][j+1]
                row.append(s)
            row.append(1)
            ans.append(row)
        return ans