import hashlib

'摘要算法MD5和SHA1'

if __name__ == '__main__':
    md = hashlib.md5()
    md.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md.hexdigest())

    # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
    md = hashlib.md5()
    md.update('how to use md5 in '.encode('utf-8'))
    md.update('python hashlib?'.encode('utf-8'))
    print(md.hexdigest())

    # SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示，SHA1更安全的算法是SHA256和SHA512
    sha = hashlib.sha1()
    sha.update('how to use sha1 in '.encode('utf-8'))
    sha.update('python hashlib?'.encode('utf-8'))
    print(sha.hexdigest())
