import json


class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = score
        self.score = score


def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }


if __name__ == '__main__':
    d = dict(name='rose', age=20, score=88)
    print(d)
    print(json.dumps(d))

    s = Student('xin', 22, 88)
    print(json.dumps(s, default=student2dict))
    # 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量，也有少数例外，比如定义了__slots__的class
    print(json.dumps(s, default=lambda obj: obj.__dict__))

    # dump()方法可以直接把JSON写入一个file-like Object
