class Student(object):
    __slots__ = ('__score', '__age')

    def __init__(self, value, age=20):
        self.__score = value
        self.__age = age

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    @property
    def age(self):
        return self.__age


if __name__ == '__main__':
    s = Student(88, 19)
    s.score = 100
    s.score = 99
    print(s.score)
    print(s.age)
    # s.age = 100
