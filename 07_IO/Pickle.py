import pickle

d = dict(name='rose', age=20, score=88)
# 把一个对象序列化到内存
print(pickle.dumps(d))

with open('test.txt', 'wb') as f:
    pickle.dump(d, f)

with open('test.txt', 'rb') as f:
    # pickle.loads()是从内存中反序列化
    d = pickle.load(f)
    print(d)