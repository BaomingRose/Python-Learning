from operator import itemgetter


def f(x):
    return x * x


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def add(x, y):
    return x + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def strToint(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# Python内建的filter()函数用于过滤序列
def is_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    # map()函数接收两个参数，一个是函数，一个是Iterable
    # map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    r = map(f, l)
    print(type(r))  # <class 'map'>
    print(list(r))  # [1, 4, 9, 16, 25, 36]

    re = reduce(add, [1, 3, 5, 7, 9])
    print(re)  # 先add(1,3)=4, 然后add(4, 5)=9……依次进行

    # Python内建的filter()函数用于过滤序列
    fil = list(filter(is_odd, l))
    print(fil)

    # sorted()  key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list
    l = [9, 3, 4, 1, 0, 5, 6, 2, 8, 7]
    new = sorted(l)
    # 排序之后list原序列是没有变化的
    print(l)
    print(new)

    # reverse这个参数表示反向排序
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

    students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(students, key=itemgetter(0)))
    print(sorted(students, key=lambda t: t[1]))
    print(sorted(students, key=itemgetter(1), reverse=True))
