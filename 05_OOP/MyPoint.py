class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x = x1
        self.y = y1

    def distance(self, other):
        dis = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dis

    def display(self):
        tup = (self.x, self.y)
        print("点坐标为：", tup)


if __name__ == '__main__':
    point1 = MyPoint(5.0, 2.0)
    point2 = MyPoint(1.0, 1.0)

    dis = point1.distance(point2)
    print("两点相距：", dis)

    point1.display()

    point1.move(0.0, 0.0)
    point1.display()


