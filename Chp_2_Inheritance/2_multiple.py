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
        response: str = Company.info(self)
        return f"Hi, I am {self.emp_name} working in {response} as an employee"


class Consultant(Company):

    def __init__(self, cmp_name, con_name):
        super().__init__(cmp_name)
        self.con_name = con_name

    def details(self):
        response: str = Company.info(self)
        return f"Hi, I am {self.con_name} working in {response} as an consultant"


obj1 = Employee("Apollo Global Management", "Mehek Jain")
obj2 = Consultant("Apollo Global Management", "Crazy Jain")
print(obj1.details())
print(obj2.details())