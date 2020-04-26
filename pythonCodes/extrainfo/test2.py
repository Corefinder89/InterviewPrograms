class Test2:
    def __init__(self):
        self.a=10
        self.__b=20

t = Test2()
print(dir(t))
