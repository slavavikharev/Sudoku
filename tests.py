#!/usr/bin/env python3

import unittest
import sudoku


class Test(unittest.TestCase):

    def check_and_return_result(self, file):
        level_str = sudoku.read_file(file)
        self.assertIsNotNone(level_str)
        level, unknown = sudoku.parse_level(level_str)
        self.assertIsNotNone(level)
        self.assertEqual(len(level_str), len(level))
        result = sudoku.solve_sudoku(level, unknown)
        return result

    def test_one(self):
        result = self.check_and_return_result("test1")
        self.assertEqual(result, [[8, 1, 5, 7, 2, 3, 6, 4, 9],
                                  [3, 4, 7, 6, 8, 9, 1, 2, 5],
                                  [6, 2, 9, 1, 4, 5, 3, 8, 7],
                                  [7, 5, 2, 8, 1, 6, 4, 9, 3],
                                  [4, 9, 8, 3, 5, 7, 2, 1, 6],
                                  [1, 6, 3, 4, 9, 2, 7, 5, 8],
                                  [2, 7, 1, 9, 6, 8, 5, 3, 4],
                                  [9, 3, 4, 5, 7, 1, 8, 6, 2],
                                  [5, 8, 6, 2, 3, 4, 9, 7, 1]])

    def test_two(self):
        result = self.check_and_return_result("test2")
        self.assertEqual(result, [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                  [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                  [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                  [3, 4, 5, 2, 8, 6, 1, 7, 9]])

    def test_three(self):
        result = self.check_and_return_result("test3")
        self.assertEqual(result, [[8, 9, 2, 7, 1, 5, 6, 3, 4],
                                  [4, 1, 5, 3, 9, 6, 7, 2, 8],
                                  [3, 7, 6, 4, 2, 8, 9, 5, 1],
                                  [7, 6, 8, 2, 5, 9, 1, 4, 3],
                                  [9, 4, 1, 8, 3, 7, 2, 6, 5],
                                  [2, 5, 3, 6, 4, 1, 8, 9, 7],
                                  [6, 8, 9, 5, 7, 3, 4, 1, 2],
                                  [1, 3, 4, 9, 8, 2, 5, 7, 6],
                                  [5, 2, 7, 1, 6, 4, 3, 8, 9]])


if __name__ == '__main__':
    unittest.main()
