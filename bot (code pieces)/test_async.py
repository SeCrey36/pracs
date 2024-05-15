from time import sleep
def fun1(x):
    print(x**2)

    # запустили ожидание
    sleep(3)

    print('fun1 завершена')


def fun2(x):
    print(x**0.5)

    # запустили ожидание
    sleep(3)

    print('fun2 завершена')


def main():
    # создали конкурентную задачу из функции fun1
    task1 = create_task(fun1(4))

    # создали конкурентную задачу из функции fun2
    task2 = create_task(fun2(4))

    # запустили задачу task1
    task1

    # запустили task2
    task2


main()