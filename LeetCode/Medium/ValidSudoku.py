# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# A partially filled sudoku which is valid.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            eachRow = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] not in eachRow:
                        eachRow.add(board[i][j])
                    else:
                        return False
        for j in range(len(board)):
            eachColumn = set()
            for i in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] not in eachColumn:
                        eachColumn.add(board[i][j])
                    else:
                        return False
        for a in range(3):
            for b in range(3):
                eachBox = set()
                for i in range(3):
                    for j in range(3):
                        if board[i+a*3][j+b*3] != '.':
                            if board[i+a*3][j+b*3] not in eachBox:
                                eachBox.add(board[i+a*3][j+b*3])
                            else:
                                return False
        return True
