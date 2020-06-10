#!/usr/bin/env python3  # 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码
# -*- coding: utf-8 -*-

' a test module '   # 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Rose' # 第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':      # # 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
    print(__doc__)      # hello模块定义的文档注释也可以用特殊变量__doc__访问
    test()

    print('命令行参数如下:')
    for i in sys.argv:
        print(i)

    print('\n\nPython 路径为：', sys.path, '\n')
