import socket

if __name__ == '__main__':
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind(('127.0.0.1', 11111))

    print('服务端启动')
    while True:
        data, addr = soc.recvfrom(1024)
        # print(type(data))     # <class 'bytes'>
        print('%s from %s' % (data.decode('utf-8'), str(addr)))

        soc.sendto(b'i have received info', addr)
