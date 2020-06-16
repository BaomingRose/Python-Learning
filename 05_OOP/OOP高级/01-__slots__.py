# 只允许对People实例添加name和age属性
class People(object):
    __slots__ = ('name', 'age')


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Student(People):
    __slots__ = ('gender')


p = People()
p.name = "rose"
p.age = 11
# p.gender = 'male'

s = Student()
s.gender = 'male'

