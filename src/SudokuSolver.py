from typing import List


class Solver:
    class Validator:
        def is_valid(self, board):

            def validate_rows():
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

            def validate_columns():
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

            def validate_boxes():
                # identify each box by the top left corner
                for i in range(0, 9, 3):
                    for j in range(0, 9, 3):
                        # now we are at the top left corner of the box to check
                        seen = [False] * 10
                        for row in range(i, i + 3):
                            for clmn in range(j, j + 3):
                                elem = board[row][clmn]
                                if not board[row][clmn].isdigit():
                                    continue

                                if seen[int(elem)]:
                                    return False
                                else:
                                    seen[int(elem)] = True

                return True

            return validate_rows() and validate_columns() and validate_boxes()

    def __init__(self, board):
        self.empty_cells = 0
        self.board = board

    def solve(self):
        # count empty cells and note down first empty cell to start
        first_empty_cell = None
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    self.empty_cells += 1
                    if first_empty_cell is None:
                        first_empty_cell = (i, j)

        def solve_cell(start):

            def get_next_empty_cell_from(cell):
                row, clmn = cell
                for i in range(row, 9):

                    # finish up the row we are in now starting from the starting clmn otherwise start at the 0 clmn
                    start_clmn = 0 if i != row else clmn + 1

                    for j in range(start_clmn, 9):
                        if self.board[i][j] == 0:
                            return i, j

            def get_candidates(cell):
                seen = [False] * 10
                seen[0] = True  # 0 is not a valid digit to be used

                def get_candidates_from_row():
                    row, clmn = cell
                    for elem in self.board[row]:
                        if elem != 0:
                            seen[elem] = True

                def get_candidates_from_column():
                    row, clmn = cell
                    for i in range(9):
                        if self.board[i][clmn] != 0:
                            seen[self.board[i][clmn]] = True

                def get_candidates_from_box():
                    # reset our start search to the top left corner of the 3x3 box we are in
                    row, clmn = cell
                    start_row = (row // 3) * 3
                    start_clmn = (clmn // 3) * 3

                    for i in range(start_row, start_row + 3):
                        for j in range(start_clmn, start_clmn + 3):
                            elem = self.board[i][j]
                            if elem != 0:
                                seen[elem] = True

                get_candidates_from_row()
                get_candidates_from_column()
                get_candidates_from_box()

                return [i for i in range(10) if not seen[i]]

            for candidate in get_candidates(start):
                row, clmn = start
                self.board[row][clmn] = candidate

                self.empty_cells -= 1
                if self.empty_cells == 0:
                    return  # we just filled in the last empty cell
                else:
                    # try candidate
                    solve_cell(get_next_empty_cell_from(start))
                    if self.empty_cells == 0:
                        return  # we've fully solved the puzzle, there's no need to try other candidates

                    # reset the cell
                    self.board[row][clmn] = 0
                    self.empty_cells += 1

        solve_cell(first_empty_cell)

        return self.board

    def __repr__(self):
        """
        Used mainly for unit testing purposes to avoid coupling with GUI
        """
        res = []
        for row in self.board:
            res.append('[' + ','.join(row) + ']')
        res = '[\n' + ',\n'.join(res) + '\n]'
        return res