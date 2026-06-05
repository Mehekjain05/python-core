class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        return f"I'm {self.name}. I'm {self.age} yrs old."

class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        person_info = Person.display_person(self)
        return f"{person_info} Here's my Student ID : {self.student_id}"

class GraduateStudent(Student):

    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic

    def display_graduate_student(self):
        student_info = Student.display_student(self)
        return f"{student_info}. Currently doing research in {self.research_topic}"


obj1 = GraduateStudent("Mehek Jain", 22, "123", "Data Science")
print(obj1.display_graduate_student())