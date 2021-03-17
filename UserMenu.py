import PySimpleGUI as sg
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

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'Solve':
                puzzle = values
                break

        # solution to puzzle will be given in a popup
        window.close()

        def format_input():
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
                if count % 9 == 0:
                    grid.append(row)
                    row = []
                    count = 0

            return grid

        return format_input()

    def output_error(self, error: str) -> None:
        pass

    def output_solution(self):
        pass