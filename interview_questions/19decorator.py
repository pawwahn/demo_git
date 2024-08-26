def common(func):
    def wrapper(a,b):
        print("first line of a function")
        func(a,b)
        print("last line of a function")
    return wrapper

@common
def add(a,b):
    print(a+b)

@common
def sub(a,b):
    print(a-b)


sub(10,20)
print("********")
add(10,20)
