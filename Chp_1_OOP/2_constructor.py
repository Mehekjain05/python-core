class MyClass:
    # instance variable
    # self => it modifies the variables for that particular object rather than modifying the class
    def __init__(self, name):
        self.name = name

    def func1(self):
        print("Hello world", self.name)

    def func2(self):
        print("You can do it")

obj = MyClass("Mehek")
obj.func1()
obj.func2()


