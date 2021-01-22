import hmac

if __name__ == '__main__':
    message = 'Hello, world!'
    key = 'secret'
    h = hmac.new(key.encode('utf-8'), message.encode('utf-8'), digestmod='MD5')

    print(h.hexdigest())

    s = '123'
    print(type(s.encode('utf-8')))  # <class 'bytes'>
    b = b'123'
    print(type(b.decode('utf-8')))  # <class 'str'>
