from isadult import is_adult
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.adult = is_adult(age)

    def greet(self):
        return f"hello ,{self.name} your are {self.age} years old"
    
    def checkadult(self):
        if self.adult:
            return f"{self.name} is an adult"
        
        return f"{self.name} is not an adult"
        

person1 = Person("alice",34)
person2 = Person("bob",12)
print(person1.name)
print(person2.age)

print(person1.greet())
print(person2.greet())
print(person1.checkadult())
print(person2.checkadult())

