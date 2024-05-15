import argparse
import sys

parser = argparse.ArgumentParser()
try:
    parser.add_argument('radius', type=float, help='Enter the radius')
    args = parser.parse_args()
except Exception as e:
    print('ERR!')
    sys.exit()
if args.radius > 0:
    d = 2*3.14*args.radius
    s = 3.24 * (args.radius**2)
    print('Len: ' + str(d) + '  S: ' + str(s))
else:
    print('Incorrect input')
