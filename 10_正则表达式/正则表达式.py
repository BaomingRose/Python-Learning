import re


# 得到邮箱的姓名
def name_of_email(addr):
    ret = re.match(r'<?(\w+\s*\w*)>?\s*\w*@\w+\.\w+', addr)
    return ret.group(1)


# 判断是否符合邮箱
def is_valid_email(addr):
    if re.match(r'^([a-z\.\#]+)@([a-z]+)\.com$', addr):
        return True
    else:
        return False


if __name__ == '__main__':
    # *表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符

    print(re.match(r'^\d{3}\-\d{3,8}$', '010-1234567'))
    print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    # 一个括号为一部分，使用group(index)，可查看每部分的内容，为0是
    print(m.group(0), m.group(1), m.group(2))

    # 切分字符串，连续的空格无法识别
    print('a b c   d'.split(' '))

    # []表示里面的任何一个字符都行，()表示匹配内容的一部分，{}表示前面的字符重复次数
    print(re.split(r'[\s\,\;]+', 'a,b; c  ;d;f'))

    t = r'15:53:06'
    m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
    if m:
        print('t是一个合法时间')
        print('hour:', m.group(1), 'minute:', m.group(2), 'second:', m.group(3))
    else:
        print('t不是一个合法时间')

    # 贪婪匹配，下面的第一部分已经全部匹配，所以第二部分没有匹配到0
    m = re.match(r'^(\d+)(0*)$', '102300')
    print(m.group(1), m.group(2))

    re.match(r'^(\d+?)(0*)$', '102300')
    print(m.groups())

    print(is_valid_email('someone@gmail.com'))
    print(name_of_email('<Tom Paris> tom@voyager.org'))
