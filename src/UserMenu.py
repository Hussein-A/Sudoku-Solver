import PySimpleGUI as sg
import copy
import Errors
from typing import List


class UserMenu:
    def __init__(self):
        sg.theme('DarkAmber')
        # All the stuff inside your window.
        row = [sg.Input(size=(3, 3)) for i in range(9)]

        self.layout = [[sg.Text('Enter digits 1-9 for each cell')]]
        for i in range(9):
            self.layout.append(copy.deepcopy(row))
        self.layout.append([sg.Button('Solve'), sg.Button('Cancel')])

    def get_sudoku(self) -> List[List[int]]:
        puzzle = []
        window = sg.Window('Sudoku Solver', self.layout)

        def format_and_verify_input():
            '''
            Firstly formats the input for use with SudokuSolver.py which expects a List[List[int]] rather than
            List[List[str]] as given by the PySimpleGui.
            Secondly verifies that the input is correctly entered. Input to cells cannot be strings and must be integers
            Also that:
                1. Each row must contain the digits 1-9 without repetition.
                2. Each column must contain the digits 1-9 without repetition.
                3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

            :return: None
            '''
            def is_valid(board):

                def validate_rows():
                    for row in board:
                        seen = [False] * 10

                        for elem in row:
                            if elem == 0:
                                continue
                            if seen[elem]:
                                return False
                            else:
                                seen[elem] = True

                    return True

                def validate_columns():
                    for clmn in range(9):
                        seen = [False] * 10

                        for row in range(9):
                            elem = board[row][clmn]
                            if elem == 0:
                                continue

                            if seen[elem]:
                                return False
                            else:
                                seen[elem] = True

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
                                    if elem == 0:
                                        continue

                                    if seen[elem]:
                                        return False
                                    else:
                                        seen[elem] = True

                    return True

                return validate_rows() and validate_columns() and validate_boxes()

            ROW_SIZE = 9
            grid = []
            row = []
            count = 0
            for key, val in values.items():
                if len(val) == 0:
                    row.append(0)
                else:
                    row.append(int(val) % 10)

                count += 1
                if count % ROW_SIZE == 0:
                    grid.append(row)
                    row = []
                    count = 0

            if not is_valid(grid):
                raise Errors.InputError('Repeated digits in board')
            return grid

        while True:
            try:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancel':
                    break
                elif event == 'Solve':
                    puzzle = values
                    format_and_verify_input()
                    break
            except Errors.Error:
                Errors.Error.popup_error()


        # solution to puzzle will be given in a popup
        window.close()

        return format_and_verify_input()
