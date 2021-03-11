import UserMenu
from typing import List

class Solver:
    class Validator:
        def is_valid(self, board: List[List[str]]) -> bool:
            return self.validate_rows(board) and self.validate_columns(board) and self.validate_boxes(board)

        def validate_rows(self, board):
            for row in board:
                seen = [False] * 10

                for elem in row:
                    if not elem.isdigit():
                        continue

                    if seen[int(elem)]:
                        return False
                    else:
                        seen[int(elem)] = True

            return True

        def validate_columns(self, board):
            for clmn in range(9):
                seen = [False] * 10

                for row in range(9):
                    elem = board[row][clmn]
                    if not board[row][clmn].isdigit():
                        continue

                    if seen[int(elem)]:
                        return False
                    else:
                        seen[int(elem)] = True

            return True
