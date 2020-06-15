

# 设计一个函数返回给定文件名的后缀名
def suffixName(filename):
    index = filename.rfind('.')
    suffix = filename[index:]
    return suffix


# 设计一个函数返回传入的列表中最大和第二大的元素的值
def max_and_max2(l):
    copy = []
    copy += l
    max1 = max(l)
    # 只会删除一个值为max1的
    copy.remove(max1)
    # print(l)
    # print(copy)
    max2 = max(copy)
    return max1, max2


# 计算指定的年月日是这一年的第几天
def countDays(year, month, day):
    mon_days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    res = 0
    for x in range(1, month):
        res += mon_days[x]

    if month > 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            res += 1
        else:
            pass

    res += day
    return res


import math


# 接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')

    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


if __name__ == "__main__":
    suffix = suffixName("hello.py")
    print(suffix)

    l = [1, 2, 3, 4, 8, 3, 4, 9, 9, 9]
    # 可以用多个值接收返回多个值得函数
    x, y = max_and_max2(l)
    # 返回多个参数，实际上是tuple
    tup = max_and_max2(l)
    print(tup)
    print("x =", x)
    print("y =", y)
    # 可以多个变量接收tuple
    m, n = tup
    print(m, n)

    year = int(input("请输入年份:"))
    month = int(input("请输入月份:"))
    day = int(input("请输入日期:"))
    res = countDays(year, month, day)
    print(res)
