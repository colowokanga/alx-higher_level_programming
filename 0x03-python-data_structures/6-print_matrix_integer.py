#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (col + 1 == len(matrix[row])):
                print("{:d}".format(matrix[row][col]), end='')
            else:
                print("{:d} ".format(matrix[row][col]), end='')
        print()
        
