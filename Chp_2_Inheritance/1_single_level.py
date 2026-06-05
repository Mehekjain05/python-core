from urllib import response


class Company:
    
    def __init__(self, cmp_name):
        self.cmp_name = cmp_name
        
    def info(self):
        return f"the company {self.cmp_name}"
    

class Employee(Company):
    
    
    def __init__(self, cmp_name, emp_name):
        super().__init__(cmp_name)
        self.emp_name = emp_name


    def details(self):
        response:str = super().info()
        return f"Hi, I am {self.emp_name} working in {response}"



obj1 = Employee( "Apollo Global Management", "Mehek Jain")
print(obj1.details())