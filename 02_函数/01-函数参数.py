def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# 必须参数
def area(width, height):
    return width * height


# 关键字参数演示
def print_welcome(str, name):
    print(str, name)


# 默认参数
def printInfo(name, age=35):
    print("名字", name)
    print("年龄", age)
    return


# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printNumber(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 加了两个星号 ** 的参数会以字典的形式导入
def printMap(arg1, **vardic):
    print(arg1)
    print(vardic)


# 如果单独出现星号 * 后的参数必须用关键字传入。
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式
def f(a, /, b, *, c):
    return a + b + c


if __name__ == '__main__':
    fib(10)

    # 必须参数
    print(area(2, 5))

    # 关键字参数，使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
    print_welcome(name="rose", str="welcome")

    printInfo("rose")

    printNumber(10, 20, 30, 40, 50, 60)

    printMap("hello", a=10, b=20)

    # *后面的参数是c，所以要使用关键字参数c=？
    d = f(1, 2, c=3)
    print(d)

    # lambda匿名函数
    sum = lambda arg1, arg2: arg1 + arg2
    print("和", sum(10, 20))
