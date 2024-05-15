"""This is a docstring which describes the program"""

import sys


def matrix_print(matrix):
    """Print matrix"""
    for i in matrix:
        print(i)


def create_mat():
    """Main function"""
    try:
        n_strs = int(input('Input N: '))
        k_cols = int(input('Input K: '))

        if 3 > k_cols or 1 > n_strs:
            print('Invalid input')
        else:
            matrix = [[0 for i in range(k_cols)] for q in range(n_strs)]
            for n_str in range(1, n_strs):
                for k in range(3, k_cols):
                    matrix[n_str][k] = 1/2 * k * \
                                       (n_str**2 + n_str) - n_str**2 + 2*n_str
            matrix_print(matrix)
            return matrix
        return None
    except ValueError:
        print('ERR while input')
        return None


def n_plus(matrix):
    """N+1 matrix"""
    for n_str in matrix:
        n_str.append(sum(n_str))
    matrix_print(matrix)
    return matrix


def k_plus(matrix):
    """K+1 matrix"""
    matrix.append([0 for i in matrix[0]])
    for k in range(len(matrix[0])):
        summ = 0
        for n_str in range(len(matrix)):
            summ += matrix[n_str][k]
        matrix[-1][k] = summ
        matrix[-1][-1] = 0
    matrix_print(matrix)
    return matrix



def main():
    '''Menu'''
    print('Hello! Its my second practical. '
          'In this program u can work with matrix')
    matrix = None
    while True:
        com = input('''
Commands: 
    1 - create matrix (recreate)
    2 - add N+1
    3 - add K+1
    4 - quit
        ''')
        if com == '4':
            sys.exit()
        elif com == '1':
            matrix = create_mat()
        elif com == '2' and matrix is not None:
            matrix = n_plus(matrix)
        elif com == '3' and matrix is not None:
            matrix = k_plus(matrix)
        else:
            print('Incorrect input or u havent matrix')


if __name__ == '__main__':
    main()
