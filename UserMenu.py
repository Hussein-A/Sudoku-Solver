import PySimpleGUI as sg
from typing import List
import copy

class UserMenu:
    def __init__(self):
        sg.theme('DarkAmber')
        # All the stuff inside your window.
        row = [sg.Input(size = (3,3)) for i in range(9)]

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

        #solution to puzzle will be given in a popup
        window.close()
        return puzzle

    def output_error(self, error: str) -> None:
        error_layout = []




    def output_solution(self):
        pass

