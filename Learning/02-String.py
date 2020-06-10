# """字符串"""或者'''字符串'''可以指定多行字符串
print("""i
am
rose""")

# 使用r可以让让反斜杠不发生转义
print(r"i\nam\nrose")

# String字面意义级联字符串
print("this" " is" " string")

# 做字符串加法
print("this" + " is" + " string")

# “，”级联，使用+和不使用都是不行的，逗号位置自动加空格
print(5, "isPrime")

# 逗号隔开，逗号位置会自动加空格
print("this", "is", "string")

# 字符串乘法，3个字符串相连
print("this " * 3)

# 字符串索引方式：从左往右以0开始，从右往左以-1开始
str = "Vegetable"
# 字符串的截取的语法格式如下：变量[头下标：尾下标：步长]
print(str)
print(str[0:-1])    # 输出第一个到倒数第二个字符
print(str[0])
print(str[-3])      # b —— 倒数第三个字符
print(str[2:5])     # get   下标为234的字符串
print(str[2:])

print()
print(str[0:5:3])   # Ve        # 从0到5的串中截取3个字符
print()

print(str[0:1:2])
print(str[::5])

# 下面的‘会被打印出来
print("hello 'world ");

# help (print)

x = "a"
y = "b"

print(x, end = ",")
print(y, end = ",")