'''
import subprocess

print('$ nslookup www.python.org')

# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出, 这和命令行直接运行的效果是一样
# 创建子进程执行 nslookup www.python.org ，然后父进程等子进程退出返回
r = subprocess.call(['nslookup', 'www.python.org'])

print('Exit code:', r)  # 返回子进程的退出码
'''


import subprocess

# 下面创建的子进程如同命令行的输入此命令
print('$ nslookup')

p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)
