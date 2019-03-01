def calc_sum():
    def sum2():
        ax = [x * x for x in range(1, 11)]
        return ax

    return sum2


# f1 = calc_sum()
# f2 = calc_sum()
# print(f1()==f2())

def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum1


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1() == f2())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def count2():
    fs = []

    def f(j):
        def g():
            return j * j

        return g

    for x in range(1, 4):
        fs.append(f(x))
    return fs


f1, f2, f3 = count2()
print(f1(), f2(), f3())


def create_counter():
    f = [0]
    print('闭包外--')

    def counter():
        print('闭包内--')
        f[0] = f[0] + 1
        return f[0]

    return counter


# 测试
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

# counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
