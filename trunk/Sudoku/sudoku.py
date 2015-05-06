#/usr/bin/env python3

import sys


def read_file(file):
    """Reads a file"""
    try:
        f = open(file)
    except FileNotFoundError:
        print("There is no this file")
        sys.exit(1)
    level_str = f.read().splitlines()
    f.close()
    return level_str


def parse_level(level_str):
    """
    Takes an abstractive sudoku, 
    returns a parsed list of lists
    """
    unknown = 0
    level = []
    for i in range(len(level_str)):
        level.append([])
        for j in range(len(level_str[i])):
            if level_str[i][j] == '0':
                level[i].append(set())
                unknown += 1
            else:
                level[i].append(int(level_str[i][j]))
    return level, unknown


def take_column(j, level):
    """Returns all numbers in a column"""
    return {i[j] for i in level if type(i[j]) == int}


def take_row(i, level):
    """Returns all numbers in a row"""
    return {j for j in level[i] if type(j) == int}


def take_square(i, j, level):
    """Returns all numbers in a square"""
    i -= i % 3
    j -= j % 3
    square = set()
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            if type(level[k][l]) == int:
                square.add(level[k][l])
    return square


def solve_sudoku(level, unknown):
    """
    The main function
    takes the level and the count of unknown cells
    returns a solved sudoku
    """
    last = str(level)
    while unknown > 0:
        for i in range(len(level)):
            for j in range(len(level[i])):
                if type(level[i][j]) == int:
                    continue
                if len(level[i][j]) == 1:
                    level[i][j] = level[i][j].pop()
                    unknown -= 1
                    continue
                level[i][j] = set()
                for a in range(1, 10):
                    if a in take_column(j, level) or \
                            a in take_row(i, level) or \
                            a in take_square(i, j, level):
                        continue
                    level[i][j].add(a)
        if str(level) == last:
            print("I can't solve it")
            sys.exit(1)
        last = str(level)
    return level


def print_result(level):
    """Just prints the sudoku"""
    for i in range(len(level)):
        level[i] = [str(j) for j in level[i]]
        if i % 3 == 0:
            print()
        print("".join(level[i][:3]) + ' ' +
              "".join(level[i][3:6]) + ' ' + "".join(level[i][6:]))


def main():
    level_str = read_file(sys.argv[1])
    level, unknown = parse_level(level_str)
    result = solve_sudoku(level, unknown)
    print_result(result)


if __name__ == "__main__":
    main()
