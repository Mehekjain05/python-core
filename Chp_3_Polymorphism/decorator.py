def decorated_func(func): #takes function as input

    def new(**kwargs): #*args -> when number of arguments will be passed is unknown
        #kwargs -> keword based arguments number passed is unknown
        print("This is new function")
        res = func(**kwargs)
        return res

    return new



@decorated_func
def og_func(**kwargs):
    print(f"Hi this is the og function and I'm {kwargs["name"]} {kwargs["surname"]}")

og_func(name = "mehek", surname = "jain", age = 22)