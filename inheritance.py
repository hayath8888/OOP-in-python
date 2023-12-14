class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

    def greet(self):
        return f"Hello, {self.name} "
    

class Student(Person):
    def __init__(self,name,age,major) -> None:
         super().__init__(name,age)
         self.major = major

    def study(self):
        return f"I am Studing {self.major}"
    

student1 = Student("john",20,"computer science")
student2 = Student("elon",21,"medical")

print(student1.name)
print(student1.major)
print(student2.age)
print(student2.study())
print(student1.greet()) 


