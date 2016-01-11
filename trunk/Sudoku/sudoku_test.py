import unittest
from sudoku import *


class SudokuTest(unittest.TestCase):
    def assertCellsEqual(self, list1, list2):
        self.assertTrue(all(c1 == c2 for c1, c2 in zip(list1, list2)))

    def test_get_col(self):
        test_sudoku = '''
        2.3.4.1
        4.1.2.3
        1.2.3.4
        3.4.1.2
        '''
        g = Grid(test_sudoku)
        expected_col = [Cell({'3'}, 1, 0),
                        Cell({'1'}, 1, 1),
                        Cell({'2'}, 1, 2),
                        Cell({'4'}, 1, 3)]
        self.assertCellsEqual(g.get_col(1), expected_col)

    def test_get_row(self):
        test_sudoku = '''
        2.3.4.1
        4.1.2.3
        1.2.3.4
        3.4.1.2
        '''
        g = Grid(test_sudoku)
        expected_row = [Cell({'1'}, 0, 2),
                        Cell({'2'}, 1, 2),
                        Cell({'3'}, 2, 2),
                        Cell({'4'}, 3, 2)]
        self.assertCellsEqual(g.get_row(2), expected_row)

    def test_get_square(self):
        test_sudoku = '''
        2.3.4.1
        4.1.2.3
        1.2.3.4
        3.4.1.2
        '''
        g = Grid(test_sudoku)
        expected_square = [Cell({'3'}, 2, 2),
                           Cell({'4'}, 3, 2),
                           Cell({'1'}, 2, 3),
                           Cell({'2'}, 3, 3)]
        self.assertCellsEqual(g.get_square(2, 2), expected_square)
        self.assertCellsEqual(g.get_square(3, 3), expected_square)
        self.assertCellsEqual(g.get_square(2, 3), expected_square)
        self.assertCellsEqual(g.get_square(3, 2), expected_square)

    def test_correct_sudoku(self):
        test_sudoku = '''
        5.3.0.0.7.0.0.0.0
        6.0.0.1.9.5.0.0.0
        0.9.8.0.0.0.0.6.0
        8.0.0.0.6.0.0.0.3
        4.0.0.8.0.3.0.0.1
        7.0.0.0.2.0.0.0.6
        0.6.0.0.0.0.2.8.0
        0.0.0.4.1.9.0.0.5
        0.0.0.0.8.0.0.7.9
        '''
        grid = Grid(test_sudoku)
        print(grid)
        self.assertTrue(grid.check_correct())

    def test_incorrect_sudoku(self):
        test_sudoku = '''
        5.3.0.0.7.0.0.0.5
        6.0.0.1.9.5.0.0.0
        0.9.8.0.0.0.0.6.0
        8.0.0.0.6.0.0.0.3
        4.0.0.8.0.3.0.0.1
        7.0.0.0.2.0.0.0.6
        0.6.0.0.0.0.2.8.0
        0.0.0.4.1.9.0.0.5
        0.0.0.0.8.0.0.7.9
        '''
        grid = Grid(test_sudoku)
        self.assertFalse(grid.check_correct())

    def test_correct_empty(self):
        test_sudoku = '''
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        0.0.0.0.0.0.0.0.0
        '''
        grid = Grid(test_sudoku)
        self.assertTrue(grid.check_correct())

    def test_random_sudoku(self):
        random_sudoku = Sudoku.random(9)
        random_sudoku = Sudoku(random_sudoku)
        random_sudoku.solve()
        self.assertTrue(random_sudoku.grid.check_correct())
        random_sudoku = Sudoku.random(16)
        random_sudoku = Sudoku(random_sudoku)
        random_sudoku.solve()
        self.assertTrue(random_sudoku.grid.check_correct())

    def test_solve_sudoku(self):
        with open('tests.txt') as file:
            for i, test_sudoku in enumerate(file):
                s = Sudoku(test_sudoku)
                s.solve()
                self.assertTrue(s.grid.check_correct())

    def test_huge_sudoku(self):
        he = '''
        16.7.8.0.1.0.11.0.5.14.9.4.12.0.15.0
        2.10.5.0.0.0.12.0.0.13.6.16.1.3.7.8
        0.0.0.0.5.0.0.0.8.7.0.0.0.14.2.16
        14.15.1.0.0.0.8.7.0.2.0.12.0.11.0.0
        15.2.11.0.0.0.9.0.4.0.0.0.13.0.0.3
        0.3.0.9.15.11.16.0.0.6.10.8.0.12.4.7
        0.16.7.0.4.0.1.0.0.0.0.13.6.8.9.14
        0.8.0.0.0.0.13.0.0.9.0.1.0.0.10.11
        0.0.0.0.11.0.10.15.13.4.0.3.0.0.1.2
        0.1.10.0.0.0.2.0.9.0.16.6.14.4.12.5
        0.0.0.16.0.0.6.5.0.0.0.2.0.0.0.13
        0.0.15.2.8.0.14.4.0.1.0.7.11.0.0.10
        10.0.12.0.0.8.0.1.0.16.0.0.0.0.0.0
        0.11.0.0.10.0.0.6.0.3.2.15.0.0.13.0
        0.14.0.1.9.15.0.0.0.8.0.10.3.6.11.0
        9.0.0.15.0.12.7.0.6.0.0.14.16.10.8.1
        '''
        s = Sudoku(he)
        s.solve()
        self.assertTrue(s.grid.check_correct())


if __name__ == '__main__':
    unittest.main()
