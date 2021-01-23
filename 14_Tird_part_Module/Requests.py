import requests

if __name__ == '__main__':
    r = requests.get('http://www.baidu.com/')
    print(r.status_code)
    # print(r.text)

    # 对于带参数的URL，传入一个dict作为params参数
    r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

    print(r.url)

    print(r.encoding)

    # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
    print(r.content)

    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
    # print(r.json())



    # 需要传入HTTP Header时，我们传入一个dict作为headers参数
    r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    print(r.content.decode('utf-8'))

    # 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
    r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
