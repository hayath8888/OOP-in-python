class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def greet(self):
        return f"hello, {self.name} you're {self.age} years old"
    
class Student(Person):
    def __init__(self, name, age,major) -> None:
        super().__init__(name, age)
        self.major=major

    def study(self):
        return f"I am Studing {self.major}"

    def greet(self):
        return super().greet()+" and "+self.study()
        

jackie=Student("jackie",23,"MBA")
nelson=Person("nelson",44)
print(jackie.greet())
print(nelson.greet())

