import base64

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据
# 对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit，把3字节的二进制数据编码为4字节的文本数据

if __name__ == '__main__':
    print(base64.b64encode(b'binary\x00string'))
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    print(base64.urlsafe_b64decode('abcd--__'))