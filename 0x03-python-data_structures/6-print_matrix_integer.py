#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for a in range(len(matrix)):
            for b in range(len(matrix[a])):
                if b != len(matrix[a]) - 1:
                    c = ' '
                else:
                    c = ''
                print("{:d}".format(matrix[a][b]), end=c)
            print()
