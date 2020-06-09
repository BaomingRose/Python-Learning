# 类型转换      当字符串内容为浮点型要转换为整型时，无法直接用 int() 转换
a = "1.1"
print(float(a))     # 1.1
print(int(float(a)))    # 1

x = y = z = 0
o, p, q = 0, 2, "rose"
print("o =", o)
print("p =", p)
print("q = " + q)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))   # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
print(isinstance(b, float))     # True
