class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Cat is eat...')


def run_twice(animal):
    animal.eat()


a = Cat()
run_twice(a)
print(dir(a))
print(hasattr(a, 'eat'))
setattr(a, 'y', 19)
print(a.y)
print(getattr(a, 'z', 404))
