"""This is a docstring which describes the program"""

import sys
import os


def alf_cfg():
    '''Function for configuring and dividing the alphabet into 2 parts'''
    # TODO: selection of alphabet of different languages
    alf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .'
    return (alf[:32], alf[32:])


def encode():
    '''Encode'''
    alf = alf_cfg()
    filenames = os.listdir()
    for i, filename in enumerate(filenames):
        print(i+1, filename)
    sel = int(input('Which file from the list should choose? '))
    with open(filenames[sel-1], encoding="utf-8") as file:
        lines = ''
        for i in file.read():
            print(i)
            lines += i

    enc_lines = ''
    for i in lines:
        if i in alf[0]:
            enc_lines += alf[1][alf[0].find(i)]
        else:
            enc_lines += alf[0][alf[1].find(i)]

    with open("otus.txt", 'w', encoding="utf-8") as file:
        file.write(enc_lines)
        file.close()


def main():
    '''Menu'''
    print('Hello! Its my 5th practical. '
          'In this program u can work with matrix')

    while True:
        com = input('''
Commands:
    1 - select file to encode (decode)
    2 - quit
        ''')
        if com == '2':
            sys.exit()
        elif com == '1':
            encode()
        else:
            print('Incorrect input or u havent matrix')


if __name__ == '__main__':
    main()
