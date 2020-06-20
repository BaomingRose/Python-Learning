import time, threading, multiprocessing


def loop():
    print('thread %s is running . . . ' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('cup数量:', multiprocessing.cpu_count())
    # 默认的主线程，名字为MainThread
    print('thread %s is running . . . ' % threading.current_thread().name)

    # 创建线程对象，target为线程运行的函数，name为线程的名字
    t = threading.Thread(target=loop, name='LoopThread')
    # 开启线程
    t.start()
    # 等待线程
    t.join()

    print('thread %s ended.' % threading.current_thread().name)