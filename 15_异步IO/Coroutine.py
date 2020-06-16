def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    # c是一个生成器，consumer函数就是一个生成器
    # 首先声明生成器，然后生产者控制生成器
    c = consumer()

    print(type(c))

    # 启动生产者-->发动生成器-->第一次停止--->生产者回到原流程-->正常运行-->发送一个n-->生成器用n来接收-->继续执行下去直到返回条件
    produce(c)
