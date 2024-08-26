class Hello:
    __variable = None

    def __new__(cls):
        if cls.__variable is None:
            cls.__variable = super().__new__(cls)
        return cls.__variable
obj1 = Hello()
obj2 = Hello()

print(obj1 is obj2)
