
# self -> using instance variable (points to the current object)
# cls -> is the class itself use it when dealing with class variables
# @classmethod -> tag or decorator (chang how function behave)


class Animal:
    national_animal = "Lion"

    def __init__(self):
        print("Welcome to the animal kingdom")

    def __str__(self):
        print("Let's find out the king of the jungle")

    @classmethod
    def _animal_type(cls, national_animal): #define it protected to let other developer know you cannot change the variable
        cls.national_animal = national_animal

    @staticmethod #static method are do not take any variables its just bounded with class
    def _nation():
        print("India")


a1 = Animal()
a1.__str__()
print(a1.national_animal)


a2 = Animal
a2._animal_type("Tiger")
print(a2.national_animal)

print(a1.national_animal)

a1._nation()

