# 练习题2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
# 具体实现方法：
import random


# random模块中的sample函数，因为这个函数有两个参数，一个是population，一个是k。其中population指定所要产生随机序列的原序列，k指定所要产生随机序列的位数
def getVerification(x):
    list1 = [a for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
    list2 = [b for b in '0123456789']
    # list2 = [b for b in range(10)]  # 这样list2中则为数字number类型，"".join(l)中有数字会错误的
    list3 = list1 + list2

    print('验证码为：', end='')
    # 从list3中随机选择x个元素构成新的list
    l = random.sample(list3, x)
    # print(type(l))    # list

    s = ''.join(l)
    print(s)


if __name__ == '__main__':
    '''
    while 1:
        x = int(input('请输入验证码的位数:'))

        getVerification(x)
    '''

    l1 = [x * x for x in range(1, 11)]
    print(l1)

    l2 = [x * x for x in range(1, 11) if x % 2 == 0]
    print(l2)

    l3 = [m + n for m in 'ABC' for n in 'XYZ']
    print(l3)

    l4 = [x if x % 2 == 0 else -x for x in range(1, 11)]
    print(l4)

    l5 = ['Hello', 'World', 18, 'Apple', None]
    # 将l5中的字符串变为小写赋给l6
    l6 = [s.lower() for s in l5 if isinstance(s, str)]
    print(l5)
    print(l6)
