import itertools
import time

if __name__ == '__main__':
    '''
    # 第二个参数是步长，从1,11,21……无限打印
    ic = itertools.count(1, 10)
    for x in ic:
        time.sleep(0.2)
        print(x)
    '''

    ic = itertools.count(1)
    # 找出ic中小于等于10的序列
    ns = itertools.takewhile(lambda x: x<=10, ic)
    # print(type(ns))     # <class 'itertools.takewhile'>
    print(list(ns))

    '''
    # 循环打印三个字符
    cs = itertools.cycle('ABC')
    for c in cs:
        time.sleep(0.2)
        print(c)
    '''

    # 第二个参数限定重复次数
    ns = itertools.repeat('A', 3)
    for n in ns:
        print(n)

    # chain可以把一组迭代对象串联起来，形成一个更大的迭代器
    for c in itertools.chain('ABC', 'XYZ'):
        print(c)

    # 把相邻重复元素跳出来构成(key, itertools._grouper)，itertools使用list强转
    for key, group in itertools.groupby("AABBBBVVVVVDDDDDFFFFF"):
        # print(type(key))         # <class 'str'>
        # print(type(group))      # <class 'itertools._grouper'>    这种类型不能直接打印，
        # print(group)               # <itertools._grouper object at 0x000001D47FB92790>
        print(key, list(group))
