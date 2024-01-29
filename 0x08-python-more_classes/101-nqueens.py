#!/usr/bin/python3
""" Queen's Gambit """


import sys


class nqueens:
    def __init__(self, n):
        self.n = n
        self.carre = [-1] * n
        self.soluce = []

    def solver(self):
        self.solving(0)
        return self.soluce

    def solving(self, column):
        if column == self.n:
            self.soluce.append(list(self.carre))
            return True

        for line in range(self.n):
            if self.is_ok(line, column):
                self.carre[column] = line
                self.solving(column + 1)
                self.carre[column] = -1

    def is_ok(self, line, column):
        for i in range(column):
            if self.carre[i] == line or\
                    abs(self.carre[i] - line) == column - i:
                return False
        return True

    def print_soluce(self):
        for soluce in self.soluce:
            print("[", end="")
            for i in range(len(soluce)):
                print("[{}, {}]".format(i, soluce[i]), end="")
                if i != len(soluce) - 1:
                    print(", ", end="")
            print("]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    n = int(sys.argv[1])
    n_queens = nqueens(n)
    soluce = n_queens.solver()
    n_queens.print_soluce()
