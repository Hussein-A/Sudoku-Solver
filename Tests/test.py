import unittest
import src.SudokuSolver as SudokuSolver


def puzzle_converter(puzzle):
    """
    converts a string format of a sudoku puzzle either of the form '...5..23..1...'
    or '00050023001000'
    where each dot/0 represents an empty cell and the string has length 81 (one for each cell of a Sudoku puzzle)

    String is converted to List[List[str]] type taken by Solver class. Specifically each elem is either a digit
    (in str form) or a period. With 9 rows and each row having 9 elements.
    :param puzzle:
    :return List[List[str]]:
    """

    board = []
    row = []
    for elem in puzzle:
        if elem == '.':
            row.append(0)
        else:
            row.append(int(elem))

        if len(row) == 9:
            board.append(row)
            row = []

    return board


class Easy(unittest.TestCase):
    def test_easy1(self):
        board = puzzle_converter('.365....9...........91.254...3.81..6...62....9....3.......5..8...8...3..215..96..')

        solver = SudokuSolver.Solver(board)
        solver.solve()

        solution = puzzle_converter('436578219521394768879162543753981426184625937962743851397456182648217395215839674')
        self.assertEqual(solver.board, solution)

    def test_easy2(self):
        board = puzzle_converter('9..5..6......67.....79.1....632.57...9.........2193...5..6...9.....89.5.......31.')

        solver = SudokuSolver.Solver(board)
        solver.solve()

        solution = puzzle_converter('941528673358467921627931548163245789495876132872193465534612897716389254289754316')
        self.assertEqual(solver.board, solution)

    def test_easy3(self):
        board = puzzle_converter('2.19..4.8..9..4.7..7..2.....87.65...9..1.......5....6....89.....9..417....25.....')

        solver = SudokuSolver.Solver(board)
        solver.solve()

        solution = puzzle_converter('261957438839614275574328619387465921946132587125789364753896142698241753412573896')
        self.assertEqual(solver.board, solution)

    def test_easy4(self):
        board = puzzle_converter('.231..8..5...8..3.8....7..11..7...942.4..1..7.....5...43.............5..7.9.5...8')

        solver = SudokuSolver.Solver(board)
        solver.solve()

        solution = puzzle_converter('923164875571982436846537921158723694264891357397645182435218769682479513719356248')
        self.assertEqual(solver.board, solution)

    def test_easy5(self):
        board = puzzle_converter('9.............6.4..2...47...4.9.5..6..98....3..67.28.9...2...3.5....7....7......4')

        solver = SudokuSolver.Solver(board)
        solver.solve()

        solution = puzzle_converter('914578362387126945625394781748935216259861473136742859461289537593417628872653194')
        self.assertEqual(solver.board, solution)


if __name__ == '__main__':
    unittest.main()
