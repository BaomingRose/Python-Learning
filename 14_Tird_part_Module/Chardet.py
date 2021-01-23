import chardet

'使用chardet来检测编码，简单易用'

if __name__ == '__main__':
    print(chardet.detect(b'Hello!'))

    data = '哈喽'.encode('gbk')
    print(chardet.detect(data))

    data = '哈喽'.encode('utf-8')
    print(chardet.detect(data))

    data = '最新の主要ニュース'.encode('euc-jp')
    chardet.detect(data)

''' 运行结果
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
{'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
{'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
'''
