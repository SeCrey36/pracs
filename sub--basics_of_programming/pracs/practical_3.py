"""Module encode/decode

This module can be used for encode and decode strings"""
import sys


def encode(temp):
    '''
    Function for configuring and dividing the alphabet into 2 parts.

    This function is necessary to configure the alphabet for further work with it

    Returns:
    tuple with 2 strings with split alphabet
    '''
    enc_str = ''
    cnt = 1
    for i in range(1, len(temp)):
        if temp[i-1] == temp[i]:
            cnt += 1
        else:
            enc_str += temp[i-1] + str(cnt)
            cnt = 1
    enc_str += temp[-1] + str(cnt)
    enc_str = enc_str.replace('1', '')
    return enc_str


def decode_last_encode(encode_str):
    """Function of decode

    Anti encode function"""
    temp = ''
    for i, sym in enumerate(encode_str):
        if sym.isdigit():
            temp += encode_str[i-1] * (int(sym)-1)
        else:
            temp += sym
    return temp



def main():
    """Menu

    Select action, print strings in console"""
    print('Hello! Its my 3rd practical. '
          'In this program u can encode string')
    encode_str = None
    while True:
        com = input('''
Commands:
    1 - input string and encode
    2 - decode string from input
    3 - quit
        ''')
        if com == '3':
            sys.exit()
        elif com == '1':
            temp = input('Input ur str for encode: ')
            if temp.isalpha():
                encode_str = encode(temp)
                print(encode_str)
            else:
                print('string must have not numbers!')
        elif com == '2' and encode_str is not None:
            print(decode_last_encode(encode_str))
        else:
            print('Incorrect com / '
                  'U call decode string from input before input')


if __name__ == '__main__':
    main()
