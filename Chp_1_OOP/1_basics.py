class MyClass:
    #class variables
    name = "Mehek"

    def func1(self):
        print("Hello world", self.name)

    def func2(self):
        print("You can do it")

obj = MyClass()
obj.func1()
obj.func2()