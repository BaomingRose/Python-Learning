import socket
import threading
import time


# 创建线程处理连接
def doLink(sock, addr):
    print('Connection Success，addr: %s' % str(addr))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        # print(data)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(b'Hello, %s!' % data.decode('utf-8').encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    # AF_INET表示ipv4，SOCK_STREAM表示面向字节流，和Linux网络编程相同
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定套接字，IP地址（本机地址）和端口，绑定窗口为一个参数，参数是一个元组
    soc.bind(('127.0.0.1', 9999))

    # 指定等待连接的最大数量
    soc.listen(5)
    print('New Connection Come! Waiting for connection ...')

    while True:
        # 新的连接的套接字，和对方的ip
        sock, addr = soc.accept()
        print(addr)

        # 创建新的进程来处理连接
        t = threading.Thread(target=doLink, args=(sock, addr))
        t.start()


