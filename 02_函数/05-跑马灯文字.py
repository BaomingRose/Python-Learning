# 练习题1：在屏幕上显示跑马灯文字
# 具体实现方法：
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        i = os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)

        # 精髓
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
