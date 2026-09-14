# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.


# Example 1:

# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


# Constraints:

#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit 1-9 or '.'.


# LeetCode: 36. Valid Sudoku : https://leetcode.com/problems/valid-sudoku/description/

import collections

# from collections import defaultdict
from time_decorator import time_decorator


class Solution1:
    @time_decorator
    def bruteForeceisValidSudoku(self, board: list[list[str]]) -> bool:
        # brute force solution
        # Check each row
        for row in range(len(board)):
            row_check = self.basic_row_check(board[row])
            if not row_check:
                return False

        col_check = self.basic_column_check(board)
        if not col_check:
            return False

        sub_box = self.check_sub_boxes(board)
        if not sub_box:
            return False

        return True

    def basic_row_check(self, l: list[str]) -> bool:
        # for i in range(len(l)):
        #     for j in range(i + 1, len(l)):
        #         if l[i] != "." and l[i] == l[j]:
        #             return False
        # return True
        s = set()
        for i in range(len(l)):
            if l[i] in s:
                return False
            if l[i] != ".":
                s.add(l[i])
        return True

    def basic_column_check(self, l: list[list[str]]) -> bool:
        for row in range(len(l)):
            column = [l[col][row] for col in range(len(l))]
            row_check = self.basic_row_check(column)
            if not row_check:
                return False
            # print(column)
        return True

    def check_sub_boxes(self, l: list[list[str]]) -> bool:
        # Make 9 boxes
        box1, box2, box3, box4, box5, box6, box7, box8, box9 = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for row in range(3):
            for col in range(3):
                box1.append(l[col][row])
            for col in range(3, 6):
                box4.append(l[col][row])
            for col in range(6, 9):
                box7.append(l[col][row])

        for row in range(3, 6):
            for col in range(3):
                box2.append(l[col][row])
            for col in range(3, 6):
                box5.append(l[col][row])
            for col in range(6, 9):
                box8.append(l[col][row])

        for row in range(6, 9):
            for col in range(3):
                box3.append(l[col][row])
            for col in range(3, 6):
                box6.append(l[col][row])
            for col in range(6, 9):
                box9.append(l[col][row])

        boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

        for box in boxes:
            row_check = self.basic_row_check(box)
            if not row_check:
                return False
        return True


class Solution2:
    @time_decorator
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)

        # Row
        for i in range(n):
            row_set = set()
            for j in range(n):
                row_elem = board[i][j]
                if row_elem in row_set:
                    return False
                if row_elem != ".":
                    row_set.add(row_elem)

        # Column
        for i in range(n):
            col_set = set()
            for j in range(n):
                col_elem = board[j][i]
                if col_elem in col_set:
                    return False
                if col_elem != ".":
                    col_set.add(col_elem)

        # Square/Box

        starts = [
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        ]

        for i, j in starts:
            square_set = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    if item in square_set:
                        return False
                    if item != ".":
                        square_set.add(item)

        return True


class Solution3:
    @time_decorator
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


valid_soduko = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

sol1 = Solution1()
sol2 = Solution2()
sol3 = Solution3()

# print(sol1.bruteForeceisValidSudoku(valid_soduko))
# print(sol1.basic_row_check(["5", "3", ".", ".", "7", ".", ".", ".", "."]))
# print(sol1.basic_column_check(valid_soduko))
# print(sol1.check_sub_boxes(valid_soduko))


print(sol1.bruteForeceisValidSudoku(valid_soduko))
print(sol2.isValidSudoku(valid_soduko))
print(sol3.isValidSudoku(valid_soduko))
