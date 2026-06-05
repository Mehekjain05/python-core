class MyClass:
    #access modifier -> public private protected
    def __init__(self, name,age,gender):
        self.name = name #public
        self.__age = age #private 
        self._gender = gender #proctected

    def func1(self):
        print("Hello world", self.name)

    def func2(self):
        print("My age is ", self.__age)

    def func3(self):
        print("My gender is ", self._gender)

obj = MyClass("Mehek", 22, 'F')
obj.name = 'meh'
obj.func1()
obj.age = 23  #you can modify the variable if its public
obj.func2()



