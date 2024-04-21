import threading
from datetime import datetime


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
    print(f'Thread {n} is finished. Spent {(end_ - start_).total_seconds()} sec')
    print(cnt)


if __name__ == '__main__':
    t1 = threading.Thread(target=count_primes, args=(1, 2, 1000001), daemon=True)
    t2 = threading.Thread(target=count_primes, args=(2, 1000001, 2000001), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
