from multiprocessing import Process
import os


# 子进程将要运行的函数
def run_proc(name):
    print('Run child process %s  (%s) . . .' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    # 创建一个进程对象，target参数为进程运行的函数，args参数为一个元组，是传入将要运行子进程函数的参数，元组一个元素时有逗号
    p = Process(target=run_proc, args=('TESTCHILD',))
    print('Child process will start.')
    # 启动子进程
    p.start()
    # 等待子进程
    p.join()

    print('Child process end.')