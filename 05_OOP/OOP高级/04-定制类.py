class Student(object):
    id = '00'
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    # 相当于Java中的toString
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # __repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
    __repr__ = __str__

    # 当一个属性不存在时，会报错，但是__getattr__()方法，动态返回一个属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # 返回一个函数也可以
        elif attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    # 定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self):
        return "My name is %s" % self.name


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        # __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


if __name__ == '__main__':
    s = Student('rose')
    print(s)  # 未定义__str__时的打印结果：<__main__.Student object at 0x000001CBE90A7400>

    print("使用__getattr__,不存在的属性(score)：", s.score)
    print("使用__getattr__,不存在的方法(age())：", s.age())
    print("使用__call__直接实例调用:", s())
    # 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
    print(callable(Student))

    for x in Fib():
        print(x)

    f = Fib()
    print(f[0])
    print(f[3])
    print(f[1: 5])

    s1 = Student('xiaoming')
    s2 = Student('xiaohong')
    s1.id = '34567'
    print(s2.id)
    print(s1(), s1.id)
    print(s2(), s2.id)
    print(s1.count)
    print(s2.count)
