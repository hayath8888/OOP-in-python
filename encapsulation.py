class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age=age

    def greet(self):
        return f"Hello, {self.__name} you're {self.__age} years old "
    

class Student(Person):
    def __init__(self,name,age,major) -> None:
         super().__init__(name,age)
         self.major = major

    def get_study(self):
        return self.__study()

    def __study(self):
        return f"I am Studing {self.major}"
    
    def greet(self):
        return super().greet()+" and "+self.__study()
    

student1 = Student("john",20,"computer science")
student2 = Student("elon",21,"medical")

print(student1.get_name())
print(student1.major)
print(student2.get_study())
print(student1.greet()) 
print(student2.greet())

bob=Person("bob",27)
print(bob.get_name())
print(bob.get_age())
bob.set_name("harry")
print(bob.get_name())