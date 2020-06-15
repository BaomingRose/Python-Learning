'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
'''


# 尾递归   在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# 汉诺塔
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


if __name__ == '__main__':
    move(4, 'A', 'B', 'C')