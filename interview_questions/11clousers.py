'''
A function inside a function is called clousers
'''

def outer_func(x):
    ls = []
    def inner_func():
        for i in range(x):
            ls.append(i)
        print(ls)
    return inner_func

closure = outer_func(5)
closure()