def add(a:int, b:int):
    return a+b

def sub(a:int, b:int):
    return a-b

def divide(a:int, b:int):
    # try:
    #     res = a/b
    # except ZeroDivisionError:
    #     return "Divide by Zero"
    # return res
    if a==0 or b==0:
        raise ZeroDivisionError("Divide by Zero")
    else:
        return  a/b


def mul(a:int, b:int):
    return a*b

