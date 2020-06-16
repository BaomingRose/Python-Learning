class Animal(object):
    def run(self):
        print("Animal is running……")


class Dog(Animal):
    def run(self):
        print("Dog is running……")

    def eat(self):
        print("Dog is eating……")


class Cat(Animal):
    def run(self):
        print("Cat is running……")

    def eat(self):
        print("Cat is eating……")


def run_twice(animal):
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()

    # 多态
    run_twice(Animal())
    run_twice(Dog())

    print(isinstance(dog, Animal))
    print(isinstance(cat, Animal))

    # getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
    setattr(dog, 'name', '旺财')
    print(hasattr(dog, 'name'))
    print(getattr(dog, 'name'))
    print(dog.name)
