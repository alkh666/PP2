class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def have_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old")

    def change_name(self, new_name):
        self.name = new_name

# create objects
p1 = Person("Alikhan", 20)
p2 = Person("Samet", 25)

# call methods
p1.greet()
p2.greet()

p1.have_birthday()
p2.change_name("Sami")
p2.greet()

# loop through multiple objects
people = [p1, p2]
for person in people:
    person.greet()