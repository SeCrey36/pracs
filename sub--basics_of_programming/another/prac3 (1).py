"""Модуль для сортировки подсчетом"""

import sys


def sort(seq):
    """Функция сортировки"""
    min_v = min(seq)
    max_v = max(seq)
    support = [0 for i in range(max_v - min_v + 1)]
    for element in seq:
        support[element - min_v] += 1
    index = 0
    for i in range(len(support)):
        for element in range(support[i]):
            seq[index] = i+min_v
            index += 1
    return seq


def main():
    """Меню"""
    print('Практическая работа 3')
    while True:
        com = input('''
Команды: 
    1 - Ввод списка чисел через пробел
    2 - Выход из программы
        ''')
        if com == '2':
            sys.exit()
        elif com == '1':
            try:
                seq = input('Вводите числа через пробел: ')
                seq = list(map(int, seq.split()))
                print(sort(seq))
            except ValueError:
                print('Некорректный ввод')
        else:
            print('Неправильно введена команда')


if __name__ == '__main__':
    main()
