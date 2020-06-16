'''
from OOP.Animal import Animal

animal = Animal()
animal.run()

print(type(Animal))     # <class 'type'>
print(type(animal))     # <class 'OOP.Animal.Animal'>
'''


def fn(self, name="world"):
    print('hello, %s' % name)

'''
要创建一个class对象，type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
# Hello = type('Hello', (object,), dict(hello=fn))    # 创建Hello class


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建,可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
    pass

