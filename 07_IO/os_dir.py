import os

if __name__ == '__main__':
    print(os.name)
    # 查看环境变量
    # print(os.environ)

    # 查看当前路径的绝对路径
    print(os.path.abspath('.'))

    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
    # 这个只是得到完整路径，并没有创建
    s = os.path.join('.', 'test')
    try:
        # 这才是创建新目录
        os.mkdir(s)
        # 这是删除目录
        # os.rmdir(s)
    except FileExistsError as e:
        print("error:", e)
        os.rmdir(s)
    except FileNotFoundError as e:
        print("error:", e)
        os.mkdir(s)

    # 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
    print(os.path.split(r'C:\Users\roseguo\PycharmProjects\Learning\IO\test.txt'))
    # 直接让你得到文件扩展名，很多时候非常方便
    print(os.path.splitext(r'C:\Users\roseguo\PycharmProjects\Learning\IO\test.txt'))

    try:
        os.rename('test10.txt', 'test.txt')
        os.remove('test1.txt')
    except FileNotFoundError as e:
        print("error:", e)

    # 列出当前目录下所有目录
    # listdir罗列当前所有文件，判断条件为文件是目录
    print([x for x in os.listdir('.') if os.path.isdir(x)])

    # 列出所有.py文件
    # 判断条件为是否为文件，然后切割出的后缀为.py
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
