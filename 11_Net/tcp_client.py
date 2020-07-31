import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 建立连接:
    s.connect(('192.168.164.129', 9999))

    # 接收欢迎消息:   以utf-8解码，因为python默认的字符串为utf-8编码
    print(s.recv(1024).decode('utf-8'))

    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))

    s.send(b'exit')
    s.close()

