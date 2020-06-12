sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
sites2 = {0, 1, 2, 3, 100, 4, 5, 0, 3, }

print(sites)   # 输出集合，重复的元素被自动去掉
print(sites2)

if 'Google' in sites :
    print("Google is in sites")
else :
    print("Google is not in sites")

a = set('abcdefghijk')
b = set('rose')

print(a)
print(a - b)    # a和b的差集
print(a | b)    # a和b的并集
print(a & b)
print(a ^ b)

