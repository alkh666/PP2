# __init__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alikhan", 20)
print(p1.name, p1.age)