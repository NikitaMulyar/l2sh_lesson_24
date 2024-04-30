from threading import Thread
import time


def count(n):
    st = time.time()
    while n > 0:
        n -= 1
    print(f'{time.time() - st}')


t1 = Thread(target=count, args=(10000000,))
t1.start()
t2 = Thread(target=count, args=(10000000,))
t2.start()
t1.join()
t2.join()

st = time.time()
count(10000000)
print(f'{time.time() - st}')