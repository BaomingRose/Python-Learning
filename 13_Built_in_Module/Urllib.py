from urllib import request, parse

if __name__ == '__main__':
    '''
    with request.urlopen('https://www.baidu.com') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
    '''

    '''
    # 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页
    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        # print(type(f.getheaders()))     # <class 'list'>
        for k, v in f.getheaders():
            print(type(k), type(v))
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    '''

    # post
    print('Login to weibo.cn...')
    email = input('Email: ')
    passwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))