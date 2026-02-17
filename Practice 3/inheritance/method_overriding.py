# method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # override
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.speak()  # Animal makes a sound
d.speak()  # Dog barks
c.speak()  # Cat meows