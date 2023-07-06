#!/usr/bin/python3
'''
nqueens backtracking program prints the coordinates of n queens,
an nxn grid such that they are in non-tracking posi
'''


from sys import argv

if __name__ == "__main__":
    x = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    # initialzes answers
    for i in range(n):
        x.append([-1, -1])

    def can_place(row, column):
        '''check if queen can be place at a given posi'''
        for i in range(row):
            if (
                x[i][1] == column
                or x[i][0] - x[i][1] == row - column
                or x[i][0] + x[i][1] == row + column
            ):
                return (True)
        return (False)

    def solve_nqueens(row):
        '''recursive backtracking funct to find the solution'''
        if row == n:
            print([[i, x[i][1] + 1] for i in range(n)])
            return

        for column in range(n):
            if can_place(row, column):
                x[row][0] = row
                x[row][1] = column
                solve_nqueens(row + 1)

    # start the recursive process at row = 0

    solve_nqueens(0)
