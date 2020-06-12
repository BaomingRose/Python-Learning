list1 = ["abcd", 786, 2.23, 'rose', 70.2]
list2 = [123, 'goerge']
print(type(list1))      # <class 'list'>

print(list1)    # ['abcd', 786, 2.23, 'rose', 70.2]
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(list2 * 2)
print(list1 + list2)

# 与Python字符串不一样的是，列表中的元素是可以改变的
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

a[0] = 10
print(a)

a[2:5] = [12, 13, 14]
print(a)

a[2:5] = []
print(a)


list = ['宋江', '吴用', '公孙胜', '关胜', '林冲', '秦明', '呼延灼', '花荣']
print(list)
list.insert(1, '卢俊义')
list.append('柴进')
print(list)

'''
for x in range(len(list)):
    if x == 0:
        print("大哥好")
    else:
        print(list[x], "兄弟好啊")
'''

for x in list:
    print(x, "兄弟好啊")