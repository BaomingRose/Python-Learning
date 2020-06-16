import functools

# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)

i = int2('10000')
print(i)

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边
print(max2(5, 6, 7))  # 10    相当于args = (10, 5, 6, 7);    max(*args)
