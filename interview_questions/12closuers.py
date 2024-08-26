def outer_func(n):
    def inner_func():
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    return inner_func

closure = outer_func(10)
print(closure)
closure()