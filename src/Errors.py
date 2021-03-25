import PySimpleGUI as sg


class Error(Exception):
    '''Base class for user-defined exceptions'''

    def __init__(self, message=None):
        self.message = 'Unspecified Error' if message is None else message
        self.error_window = sg.Window('ERROR', [[sg.Text(self.message)]])

    def popup_error(self):
        error_event, error_values = self.error_window.read()


class InputError(Error):
    '''
    Occurs when an input is incorrect. This is most likely due to the rules
    of a Sudoku board not being followed. See format_and_verify_input for more details
    as to the rules being observed.

    :param message: The specific input error (duplicate integers, non-integer in cell, etc.
    '''

    def __init__(self, message):
        super(InputError, self).__init__(message)


class ImpossibleSolutionError(Error):
    '''
    Occurs when there is no possible solution to the inputted puzzle.
    '''

    def __init__(self):
        super(ImpossibleSolutionError, self).__init__('No solution exists for this configuration.')
