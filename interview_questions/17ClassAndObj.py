class A:
    def __init__(self, a, b):
        print("Values of 'a' and 'b' are : {},{} ".format(a, b))
        
    def funcA(self, a, b):
        print(a + b)

class B:
    def __init__(self, a, b):
        print("Values of 'a' and 'b' are : {},{} ".format(a, b))

    def funcA(self, a, b):
        print(a * b)

a= A(10, 20)
a.funcA(10, 20)


#b= B(100, 200)
#b.funcA(10, 20)

