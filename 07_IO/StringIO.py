"""很多时候，数据读写不一定是文件，也可以在内存中读写"""

from io import StringIO
from io import BytesIO

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
