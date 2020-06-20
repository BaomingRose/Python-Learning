import time, threading

balance = 0
lock = threading.Lock()


def change_it(n):
    # 银行余额，先存后取
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        change_it(n)
        lock.release()


if __name__ == '__main__':
    # Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核
    t1 = threading.Thread(target=run_thread, args=(5, ))
    t2 = threading.Thread(target=run_thread, args=(8, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(balance)
