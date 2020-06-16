# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 rose 也是可以正常执行的:
class Test:
    i = 0
    s = ""

    def prt(rose, a):
        print(rose)
        print(rose.__class__)
        print(rose.__doc__)
        print(rose.__dir__())


if __name__ == '__main__':
    t = Test()
    t.prt("xxx")
    # 实例化类
    p = people('rundoc', 10, 30)
    p.speak()
