def swap(func):
    def wrapper(a,b):
        if b>a:
            a,b = b,a
        func(a,b)
    return wrapper

@swap
def divide(a,b):
    print(a/b)

divide(5,2)
divide(5,5)
divide(5,10)