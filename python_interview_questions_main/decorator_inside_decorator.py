def wrap(x):
    print(x)
    def mydecorator(func):
        def wrapper(a, b):
            print("first line")
            tot = func(a, b)
            print(tot + x)
            print("last line")
        return wrapper
    return mydecorator

@wrap(x=10)
def add(a, b):
    tot = a + b
    return tot

@wrap
def sub(a, b):
    tot = a - b
    return tot


x = add(10, 20)
# y = sub(10,20)
