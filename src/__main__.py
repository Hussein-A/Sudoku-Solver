import UserMenu
import SudokuSolver

menu = UserMenu.UserMenu()
board = menu.get_sudoku()

solver = SudokuSolver.Solver(board)
solver.solve()