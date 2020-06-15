from typing import Iterable

hero3 = hero = {'及时雨': '宋江', '玉麒麟': '卢俊义', '智多星': '吴用', '入云龙': '公孙胜', '大刀': '关胜', '豹子头': '林冲'}
print(hero)

favourite_places = {'张三': ['西湖', '灵隐寺'], '李四': ['颐和园', '故宫'], '王五': ['洞庭湖', '钱塘江']}
print(favourite_places)

print(type(hero))
print(type("hello"))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))

s = {1, 5, 6, 2, 3, 0}
print(max(s))
print(min(s))
print(s)

print(len(hero))
print(str(hero))
hero2 = hero.copy()
# hero.clear()
print(hero3)

a = b = 10
del a
# print(a)
print(b)

dict5 = {(1, 2): 1}
# dict不可放可变元素
# dict6 = {(0, [0, 10, 20]):"不ok"}
print(dict5)


# 遍历dict
for key in hero:
    print(key)

for value in hero.values():
    print(value)

for key, value in hero.items():
    print(key, value)

print(isinstance([1,2,3], Iterable))    # list是否可迭代