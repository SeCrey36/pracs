import argparse
import sys

parser = argparse.ArgumentParser()
try:
    parser.add_argument('base1', type=float, help='Enter the length of the first base')
    parser.add_argument('base2', type=float, help='Enter the length of the second base')
    parser.add_argument('height', type=float, help='Enter the length of the height')
    args = parser.parse_args()
except Exception as e:
    print('ERR!')
    sys.exit()
if args.base1>0 and args.base2>0 and args.height>0:
    k = (abs((args.base1 - args.base2)/2)**2 + args.height**2)**0.5
    p = k*2 + args.base1 + args.base2
    print(p)
else:
    print('Incorrect input')
