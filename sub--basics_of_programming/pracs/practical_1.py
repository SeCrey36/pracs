'''Wostenholme numbers detect module'''
import sys
from decimal import Decimal, getcontext
import math


def main():
    '''Main function'''
    getcontext().prec = 100000
    while True:
        w_p = input('(print "q" to exit) ')
        if w_p == 'q':
            sys.exit()
        try:
            w_p = int(w_p)
        except TypeError:
            print('Incorrect input')
            continue
        except ValueError:
            print('Incorrect input')
            continue
        w_l = (Decimal(math.factorial(2 * w_p))) / \
              (Decimal(math.factorial(w_p)) *
               Decimal(math.factorial(2 * w_p - w_p))) - Decimal(2)
        if Decimal(w_l) % (w_p ** Decimal(4)) == Decimal(0):
            print('p - число Вольстенхольма')
        if w_p % 2 == 0:
            print('p четное')


if __name__ == '__main__':
    main()
