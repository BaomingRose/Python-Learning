import socket
import time


if __name__ == '__main__':
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        s = input('和服务器说句话吧：')

        # 关键地方，将字符串类型转为字节类型，发送给服务端
        b = bytes(s, 'utf-8')
        soc.sendto(b, ('127.0.0.1', 11111))

        data, addr = soc.recvfrom(1024)
        print(data.decode('utf-8').encode('utf-8'))
