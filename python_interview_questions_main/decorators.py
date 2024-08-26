def my_decorator(func):
    def wrapper(a,b):
        print("first line")
        tot = func(a,b)
        print(tot)
        print("last line")
        return tot
    return wrapper

@my_decorator
def funcAdd(a,b):
    tot = a+b
    return tot

@my_decorator
def funcSub(a,b):
    tot = a-b
    return tot

a1 = funcSub(10,20)
print(a1)
b1 = funcAdd(20,10)



