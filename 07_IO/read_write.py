if __name__ == '__main__':
    # Python引入了with语句来自动帮我们调用close()方法
    with open('test.txt', 'r') as f:
        print(f.read())

    # 以二进制读取文件
    with open('test.txt', 'rb') as f:
        print(f.read())

    with open('test.txt', 'r') as f:
        # 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
        for line in f.readlines():
            print(line.strip())     # 使用strip将末尾的\n删除，否则每行后多一个\n

    # 每次读取2个字节，这种方式是经常使用的，如果文件过大，不可能全部加载到内存
    with open('test.txt', 'r') as f:
        s = f.read(2)
        while s:
            # print(len(s))     # 最后一次的长度可能为1
            print(s)
            s = f.read(2)

    # 这个也是防止文件过大，readlines适合读取配置文件，注意open的几个参数，读取gbk编码的文件，可能遇到UnicodeDecodeError可以忽略
    with open('test.txt', 'r', encoding='gbk', errors='ignore') as f:
        line = f.readline()
        while line:
            print(line.strip())
            line = f.readline()

    # w方式，如果文件不存在，则创建新文件写入
    with open('test1.txt', 'w') as f:
        f.write("hello, world")

    with open('test1.txt', 'w') as f:
        f.write('0000000000000000')

    # 和C语言相同，w会覆盖原文件，a会准追加原文件
    with open('test1.txt', 'a') as f:
        f.write('abcdefghijklmnopqrstuvwxy')

