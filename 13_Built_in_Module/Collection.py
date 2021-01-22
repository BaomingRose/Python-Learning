from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            # last=False
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


if __name__ == '__main__':
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)

    print(isinstance(p, Point))
    print(isinstance(p, tuple))


    # deque 为了高效实现插入和删除操作的双向列表，适合用于队列和栈
    # list是线性存储，数据量大的时候，插入和删除效率很低。
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print(q)
    q.popleft()
    q.pop()
    print(q)


    # 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
    # 除了有默认值外，其他和dict一样
    dd = defaultdict(lambda: 'N/A')
    print(dd['a'])      # key='a'不存在，所以返回默认的'N/A'


    # OrderedDict
    # 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
    # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
    od = OrderedDict()
    od['z'] = 1
    od['x'] = 2
    od['y'] = 3
    for a, b in od.items():
        print('key:', a, 'value:', b)

    lu = LastUpdatedOrderedDict(2)
    lu[1] = 'a'
    lu[2] = 'c'
    lu[3] = 'b'


    # ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找
    # 构造缺省参数:
    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v}

    # 组合成ChainMap:
    # 将命令行参数、环境变量、默认参数依次传入，将按顺序查找key值是否存在
    combined = ChainMap(command_line_args, os.environ, defaults)

    # 打印参数:
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])


    # 空字符串为假
    s = ''
    if s:
        print('空串 is true')
    else:
        print('空串 is false')


    # Counter
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
    print(c['m'])
