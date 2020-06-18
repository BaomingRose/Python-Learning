from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s  (%s) . . . ' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    # 创建一个进程池对象, Pool的默认大小是CPU的核数
    p = Pool(10)

    for i in range(11):
        # 异步
        p.apply_async(long_time_task, args=(i, ))

    print('Waiting for all subprocesses done . . . ')

    # 创建完进程就可以销毁进程池了，进程已经放到就绪队列等着跑了，进程池的任务已经完成
    p.close()
    # 等待所有子进程，用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process
    p.join()
    print('All subprocesses done.')