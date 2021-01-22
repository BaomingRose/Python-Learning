import struct

# 准确地讲，Python没有专门处理字节的数据类型。
# struct的pack函数把任意数据类型变成bytes
# Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了

if __name__ == '__main__':
    # > 表示大端字节序，I表示4字节无符号
    print(struct.pack('>I', 10240099))
    # H表示2字节无符号整数
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

    print(struct.unpack('<ccIIIIIIHH', s))