# using super() to call parent methods
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Animal: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def info(self):
        super().info()
        print(f"Breed: {self.breed}")

d = Dog("Buddy", "Labrador")
d.info()