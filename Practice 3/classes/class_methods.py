class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species

    @staticmethod
    def greet():
        print("Hello from the class!")

    def info(self):
        print(f"{self.name}, {self.age}, {self.species}")

# create objects
p1 = Person("Alikhan", 20)
p2 = Person("Samet", 25)

# call instance method
p1.info()
p2.info()

# call class method
Person.set_species("Homo sapiens")
p1.info()
p2.info()

# call static method
Person.greet()
p1.greet()
p2.greet()