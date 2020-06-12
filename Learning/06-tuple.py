
# 元组 ：元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple1 =  ('abac', 786, 2.23, 'rose', 70.2)
tuple2 = (123, 'george')

print(type(tuple1))

print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tuple2 * 2)
print(tuple1 + tuple2)

# tuple 一个元素，需要在元素后加逗号
tuple3 = (1,)
print(tuple3)

# 空元祖
tuple4 = ()

tup = (-53, 55435, 1434, 453059, 999999, 543, 34, 0)

print(max(tup))
print(min(tup))
print(len(tup))

# del tup

# tup[0] = 30   # tuple的元素不可以更改

l = list(tup)
l[0] = 30
print(l)