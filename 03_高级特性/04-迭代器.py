# 直接作用for循环的数据类型
# 集合数据类型，如list、tuple、dict、set、str等；
# generator，包括生成器和带yield的generator function。
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable

from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))

for x in [1, 2, 3, 4, 5]:
    print(x, end=" ")
print()

# 这两种遍历方式等价

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        print(next(it), end=" ")
    except StopIteration:
        # 遇到StopIteration就退出循环
        break