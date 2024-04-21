from multiprocessing import Process, Queue
from datetime import datetime


q = Queue()


def count_primes(n, st, end):
    def is_prime(num):
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
        return True

    cnt = 0
    start_ = datetime.now()
    for i in range(st, end):
        if is_prime(i):
            cnt += 1
    end_ = datetime.now()
    print(f'Process {n} is finished. Spent {(end_ - start_).total_seconds()} sec')
    q.put(cnt)


def main():
    p1 = Process(target=count_primes, args=(1, 2, 1000001), daemon=True)
    p2 = Process(target=count_primes, args=(2, 1000001, 2000001), daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    while not q.empty():
        print(q.get())


def sync():
    def is_prime(num):
        for i in range(2, int(num ** 0.5 + 1)):
            if num % i == 0:
                return False
        return True
    cnt = 0
    start_ = datetime.now()
    for i in range(2, 2000000):
        if is_prime(i):
            cnt += 1
    end_ = datetime.now()
    print(f'Process {0} is finished. Spent {(end_ - start_).total_seconds()} sec')
    print(cnt)


if __name__ == '__main__':
    sync()
    main()
