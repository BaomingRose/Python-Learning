import sys
from contextlib import contextmanager, closing
from urllib.request import urlopen

'''
# 以下三种情况实现with:
# 第一种调用' with 构造函数 as 对象变量 ', 是通过类的成员方法实现
# 第二种调用' with 其他函数(yield 对象) as 对象变量 ', 这个其他函数是一个@注释，并且作为生成器，yield一个对象
# 第三种调用' with 其他函数 ', 这个其他函数和第二种不同的地方是yield不返回一个变量，yield前的代码是with前执行的，with结束后执行yield后面的代码

# 第一种情况
'任何对象，只要正确实现了上下文管理，就可以用于with语句，实现上下文管理是通过__enter__和__exit__这两个方法实现的'


# 可以直接调用对象的构造来构造对象
class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)
'''

# 第二种情况
'编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下:'
class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


# 可以通过其他函数来生成对象, 生成器实现
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


# 第三种情况
# 并不返回对象，而是想在with内容前后做一些动作
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


# 如果没有实现上下文就不能使用with，可以用contextlib的closing对象

if __name__ == '__main__':
    '''
    # 第一种使用
    with Query('rose') as q:
        q.query()
    '''

    # 第二种使用
    with create_query('rose') as q:
        q.query()

    # 第三种使用
    with tag("h1"):
        print("hello")
        print("world")

    with closing(urlopen('http://www.yahoo.com')) as f:
        print(type(f))     # <class 'http.client.HTTPResponse'>
        with open('./tmp.txt', 'wb') as fil:
            for line in f:
                fil.write(line)
                # sys.stdout.write(line)
                print(line)
