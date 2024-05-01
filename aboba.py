from threading import Thread, Semaphore
from time import sleep

a = 5
b = 10

s = Semaphore(4)


def function_a():
    s.acquire()
    print('Функция a, 1 заблокирован')
    sleep(2)

    s.acquire()
    print('Функция a, 2 заблокирован')
    sleep(2)

    s.release()
    print('Функция a, 2 разблокирован')
    sleep(2)

    s.release()
    print('Функция a, 1 разблокирован')
    sleep(2)


def function_b():
    s.acquire()
    print('Функция b, 1 заблокирован')
    sleep(2)

    s.acquire()
    print('Функция b, 2 заблокирован')
    sleep(2)

    s.release()
    print('Функция b, 2 разблокирован')
    sleep(2)

    s.release()
    print('Функция b, 1 разблокирован')
    sleep(2)


t1 = Thread(target=function_a)
t2 = Thread(target=function_b)

t1.start()
t2.start()

t1.join()
t2.join()

print('Готово')