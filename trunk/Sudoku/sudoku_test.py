import unittest

from sudoku import *


class SudokuTest(unittest.TestCase):
    def assertCellsEqual(self, list1, list2):
        self.assertTrue(all(c1 == c2 for c1, c2 in zip(list1, list2)))

    def test_get_col(self):
        test_sudoku = '''
        2341
        4123
        1234
        3412
        '''
        g = Grid(test_sudoku)
        expected_col = [Cell({'3'}, 1, 0),
                        Cell({'1'}, 1, 1),
                        Cell({'2'}, 1, 2),
                        Cell({'4'}, 1, 3)]
        self.assertCellsEqual(g.get_col(1), expected_col)

    def test_get_row(self):
        test_sudoku = '''
        2341
        4123
        1234
        3412
        '''
        g = Grid(test_sudoku)
        expected_row = [Cell({'1'}, 0, 2),
                        Cell({'2'}, 1, 2),
                        Cell({'3'}, 2, 2),
                        Cell({'4'}, 3, 2)]
        self.assertCellsEqual(g.get_row(2), expected_row)

    def test_get_square(self):
        test_sudoku = '''
        2341
        4123
        1234
        3412
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
        530070000
        600195000
        098000060
        800060003
        400803001
        700020006
        060000280
        000419005
        000080079
        '''
        grid = Grid(test_sudoku)
        self.assertTrue(grid.check_correct())

    def test_incorrect_sudoku(self):
        test_sudoku = '''
        530070005
        600195000
        098000060
        800060003
        400803001
        700020006
        060000280
        000419005
        000080079
        '''
        grid = Grid(test_sudoku)
        self.assertFalse(grid.check_correct())

    def test_correct_empty(self):
        test_sudoku = '''
        000000000
        000000000
        000000000
        000000000
        000000000
        000000000
        000000000
        000000000
        000000000
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
        0G0VCUB0TPR0EXOIA00Y0HKJ0
        0S000O0KV0AH000MU00P0000N
        00KN000R0AL00Y0C0QW0M000U
        EYB0QM0W0HI0JU00KS0L00000
        RAUD0GQ000000T00X0V00LWPO
        0E0G0TF0P00YALJ0000K0X00S
        0FR0T000BGEVKQ0S0XJC0000D
        00SY0V0E00000RCG0P0B00OFJ
        L0000D000SFTG0N00VO0C00HB
        BVCJDLRM00000OHW00YAP00G0
        VCW0PAYFH00ET00000SD0Q0OL
        A00U00C00XYJ00V000KFNDMW0
        H0D0JPL0K000N000G0IVF0C0E
        0LGENSM000C00IXQ00A00V00T
        KB0F0EW00000SH00TCMUY0PAG
        0K00VIU00DHQ00000FTEOPLSX
        QT00U0GP00V0RDFN000I0000A
        IPH00X0Q0ENM00000B0J0RU00
        G0000HTN0J0IUEAVP000W0FQ0
        D00L0K0000OPXJ00M0QH0C0N0
        FNEB00K0G00X000000PM0YSRW
        00000W0UY00LH0RF0I0GV0NXP
        U000I0PH0O0G00YD0K000FT00
        S0000J00EF000MK0RN0Q000L0
        0RPO0N00QMDUC0EAY0XWJI0K0
        '''
        s = Sudoku(he)
        s.solve()
        self.assertTrue(s.grid.check_correct())


if __name__ == '__main__':
    unittest.main()
