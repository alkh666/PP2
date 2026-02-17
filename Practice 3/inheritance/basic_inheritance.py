# basic inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Dog inherits from Animal
class Dog(Animal):
    pass

a = Animal("Generic")
d = Dog("Buddy")

a.speak()  # Generic makes a sound
d.speak()  # Buddy makes a sound (inherited)