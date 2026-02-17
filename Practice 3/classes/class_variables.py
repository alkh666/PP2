class Person:
    species = "Human"  # class variable shared by all objects

    def __init__(self, name, age):
        self.name = name   # instance variable unique per object
        self.age = age

# create objects
p1 = Person("Alikhan", 20)
p2 = Person("Samet", 25)

# access class and instance variables
print(p1.name, p1.age, p1.species)
print(p2.name, p2.age, p2.species)

# modify instance variable
p1.age = 21
print(p1.name, p1.age)

# modify class variable
Person.species = "Homo sapiens"
print(p1.species, p2.species)

# add new instance variable dynamically
p1.country = "Kazakhstan"
print(p1.country)