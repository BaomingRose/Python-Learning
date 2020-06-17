import pdb

'''     # 捕获异常并处理，finally一定会执行
try:
    print('try……')
    # r = 10 / 1
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally……')

print('end!')
'''

'''     # 捕获多种异常，如果没有异常else
try:
    print('try...')
    # r = 10 / int('a')
    r = 10 / int('1')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
'''


'''     # Python内置的logging模块可以非常容易地记录错误信息
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
'''


'''
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    # 捕获错误目的只是记录一下，便于后续追踪，raise语句如果不带参数，就会把当前错误原样抛出
    except ValueError as e:
        print('ValueError!')
        raise

bar()
'''

'''     # 使用pdb调试并联系使用pycharm调试器
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
'''

import logging
logging.basicConfig(level=logging.INFO)

# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
