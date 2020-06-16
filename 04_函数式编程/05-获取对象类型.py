import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

print(isinstance(fn, types.FunctionType))

# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

print('ABC'.__len__())
print(len('ABC'))

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
