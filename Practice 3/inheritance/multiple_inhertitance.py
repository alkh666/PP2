# multiple inheritance
class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()   # Can fly
d.swim()  # Can swim