from typing import List
from collections import Counter
from itertools import product


class Solution:

    def _board_to_ints(self, board: List[List[str]]) -> bool:
        out = []
        for row in board:
            out.append([int(el.replace(".", "0")) for el in row])
        return out

    def _validate_rows(self, board: List[List[int]]) -> bool:
        check = True
        for row in board:
            row = [x for x in row if x != 0]
            if len(row) == 0:
                continue
            check = check and max(Counter(row).values()) <= 1
        return check

    def _validate_cols(self, board: List[List[int]]) -> bool:
        check = True
        for i in range(9):
            col = [row[i] for row in board]
            col = [x for x in col if x != 0]
            if len(col) == 0:
                continue
            check = check and max(Counter(col).values()) <= 1
        return check

    def _extract_square(self, board: List[List[int]], k: int, l: int) -> List[
        int]:
        out = []
        for i, j in product([k, k + 1, k + 2], [l, l + 1, l + 2]):
            out.append(board[i][j])
        # print(f"square {out=}")
        return out

    def _validate_squares(self, board: List[List[int]]) -> bool:
        check = True
        for k, l in product([0, 3, 6], [0, 3, 6]):
            square = self._extract_square(board, k, l)
            square = [x for x in square if x != 0]
            if len(square) == 0:
                continue
            check = check and (max(Counter(square).values()) <= 1)
        return check

    def isValidSudoku(self, board: List[List[int]]) -> bool:

        board = self._board_to_ints(board)
        # print(f"{board=}")

        # 1. validate rows
        rows_check = self._validate_rows(board)
        # print(f"{rows_check=}")
        # 2. validate columns
        cols_check = self._validate_cols(board)
        # print(f"{cols_check=}")
        # 3. validate squares
        squares_check = self._validate_squares(board)
        # print(f"{squares_check=}")

        return rows_check and cols_check and squares_check
