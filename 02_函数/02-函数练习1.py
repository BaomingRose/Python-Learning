def maxCommanFactor(num1, num2):
    tmp = 0
    while num2 != 0:
        tmp = num1
        num1 = num2
        num2 = tmp % num2
    return num1


# 和C一样，是不会改变参数的值得
def test(a, b):
    a = 10
    b = 100

    a, b = b, a + b  # b依然使用的原来的a
    print(a)
    print(b)


# 判断素数
def isPrime(a):
    for x in range(2, int(a ** 0.5 + 1)):
        if a % x == 0:
            print(a, "%", x, "==0")
            return False
    return True


# 判断回文
def judgePlalindrome(a):
    l = []
    l += a
    a.reverse()
    if l == a:
        return True
    else:
        return False


def judgePlalindromePrime(a):
    if isPrime(a) and judgePlalindrome(list(str(a))):
        return True
    else:
        return False


if __name__ == '__main__':
    a = 3000
    b = 5000
    test(a, b)
    print(a, b)
    '''
    while True:
        a = int(input("请输入一个整数:"))
        if judgePlalindromePrime(a):
            print(a, "是回文素数")
        else:
            print(a, "不是回文素数")
    '''
    while True:
        print("请输入两个数字：")
        a = int(input())
        b = int(input())
        num = maxCommanFactor(a, b)
        print(a, "和", b, "的公因数为", num)
