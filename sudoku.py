import argparse
from itertools import chain
from random import randint, sample
from re import findall
from string import ascii_uppercase, digits

__all__ = ['Cell', 'Grid', 'Sudoku']


class Cell:
    def __init__(self, values, x, y):
        """
        :type values: set
        """
        self.values = values
        self.coord = (x, y)
        self.size = len(values)
        self.fixed = self.size == 1

    def __str__(self):
        return ''.join(self.values)

    def __len__(self):
        return self.size

    def __eq__(self, other):
        return self.values == other.values and \
               self.coord == other.coord

    def copy(self):
        """Returns a copy of this cell"""
        return Cell(self.values, *self.coord)

    def change_values(self, values):
        """
        Changes values for this cell;
        Calculates new size;
        Determines if this cell is fixed now
        :param values:
        """
        self.values = values
        self.size = len(values)
        self.fixed = self.size == 1


class Grid:
    def __init__(self, values=None):
        """
        :type values: str
        """
        if values is None:
            return
        values = ''.join(row.strip() for row in values.splitlines())
        n = len(values) ** .25
        if not n.is_integer():
            raise ValueError("The count of elements should be square")
        self.n = int(n) ** 2
        if self.n == 9 or self.n == 4:
            self.digits = digits[1:][:self.n]
        elif self.n == 16:
            self.digits = (digits[1:] + ascii_uppercase)[:self.n]
        elif self.n == 25:
            self.digits = ascii_uppercase[:self.n]
        else:
            raise ValueError("Only 9x9, 16x16 or 25x25 sudoku")
        self.digits = set(self.digits)
        self._grid = [[Cell({cell} if cell not in '.0' else self.digits, x, y)
                       for x, cell in enumerate(row)]
                      for y, row in enumerate(findall('.' * self.n, values))]

    def __str__(self):
        return '\n'.join(' '.join([str(cell) for cell in row])
                         for row in self._grid)

    def __getitem__(self, indexes):
        """
        :type indexes: tuple (int, int) or (slice, slice)
        """
        if all(isinstance(index, int) for index in indexes):
            return self._grid[indexes[1]][indexes[0]]
        return [cell for row in self._grid[indexes[1]]
                for cell in row[indexes[0]]]

    def __iter__(self):
        return (cell for cell in self[:, :])

    def get_row(self, row):
        """Returns all cells in 'row' row
        :param row:
        """
        return self[:, row:row + 1]

    def get_col(self, col):
        """Returns all cells in 'col' col
        :param col:
        """
        return self[col:col + 1, :]

    def get_square(self, x, y):
        """Returns all cells in x&y's square
        :param x:
        :param y:
        """
        n = int(self.n ** .5)
        sqr_x = x - x % n
        sqr_y = y - y % n
        return self[sqr_x:sqr_x + n,
                    sqr_y:sqr_y + n]

    def get_peers(self, x, y):
        """
        Returns all cells in col, row
        and square for x&y's cell
        :param x:
        :param y:
        """
        units = chain(self.get_col(x),
                      self.get_row(y),
                      self.get_square(x, y))
        return filter(lambda c: c != self[x, y], units)

    def possible(self, x, y):
        """Returns possible values for x&y's cell
        :param x:
        :param y:
        """
        impossible_values = {next(iter(c.values))
                             for c in self.get_peers(x, y)
                             if c.fixed}
        return self.digits - impossible_values

    def delete_bad(self):
        """
        Deletes all impossible values
        in each cell in this grid;
        Returns True if it's possible else False
        """
        for cell in (c for c in self if not c.fixed):
            possible = self.possible(*cell.coord)
            if not possible:
                return False
            self[cell.coord].change_values(possible)
            if self[cell.coord].fixed:
                return self.delete_bad()
        return True

    def check_correct(self):
        """
        Returns whether all fixed
        cell have possible values
        """
        return all(next(iter(c.values))
                   in self.possible(*c.coord)
                   for c in self if c.fixed)

    def copy(self):
        """Returns a copy of this grid"""
        new = Grid()
        new.n = self.n
        new.digits = self.digits
        new._grid = [[cell.copy() for cell in row]
                     for row in self._grid]
        return new


class Sudoku:
    def __init__(self, values):
        """
        :type values: str
        """
        self.grid = Grid(values)
        if not self.grid.check_correct() or \
                not self.grid.delete_bad():
            raise ValueError("Sudoku is not correct")

    def __str__(self):
        return str(self.grid)

    def solve(self):
        """Make this sudoku solved"""
        self.grid = self.search(self.grid)

    def search(self, grid):
        """
        Returns solved sudoku's grid
        :param grid:
        """
        if all(c.fixed for c in grid):
            return grid
        c = min((cell for cell in grid if not cell.fixed), key=len)
        for d in sample(c.values, c.size):
            new_grid = grid.copy()
            new_grid[c.coord].change_values({d})
            if not new_grid.delete_bad():
                continue
            solved = self.search(new_grid)
            if solved:
                return solved

    def desolve(self):
        """
        Returns this unsolved
        sudoku in string format
        """
        if not all(c.fixed for c in self.grid):
            raise ValueError("Sudoku must be solved")
        return ''.join(str(cell) if randint(0, 1) else '0'
                       for cell in self.grid)

    @staticmethod
    def random(n):
        """
        Returns random generated
        sudoku with size 'n'
        :param n:
        """
        sudoku = Sudoku('0' * n ** 2)
        sudoku.solve()
        return sudoku.desolve()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument_group('')
    parser.add_argument('--file', metavar='FILE',
                        help='solve from file', type=str)
    parser.add_argument('--many', action='store_true',
                        help='solve all sudoku from file')
    parser.add_argument('--random', metavar='N', choices={4, 9, 16, 25},
                        help='generate sudoku NxN', type=int)
    args = parser.parse_args()

    if args.file:
        with open(args.file) as file:
            if args.many:
                for line in file:
                    s = Sudoku(line)
                    s.solve()
                    print("%s\n" % s)
            else:
                s = Sudoku(file.read())
                s.solve()
                print(s)

    if args.random:
        print(Sudoku.random(args.random))
