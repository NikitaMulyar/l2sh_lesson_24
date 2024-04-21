from threading import Thread
from time import sleep

counter = 0


def increase(by, n):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)
    # Передаем ОС управлением над потоками

    counter = local_counter
    print(f'{n}. {counter=}')


t1 = Thread(target=increase, args=(10, 1))
t2 = Thread(target=increase, args=(20, 2))
t1.start()
t2.start()
t1.join()
t2.join()
