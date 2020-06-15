import sys

# 一边循环一边计算的机制
g = (x * x for x in range(10))
print(type(g))  # <class 'generator'> 生成器

# 可以通过next()函数获得generator的下一个返回值
# 可以使用for循环
for n in g:
    print(n)


# generator的另一种方法, 函数定义中包含yield关键字
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    # except StopIteration:
        # sys.exit()
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
