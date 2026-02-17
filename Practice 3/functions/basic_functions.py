# simple functions
def greet():
    print("Hello!")

def welcome(name):
    print(f"Welcome, {name}!")

greet()
welcome("Alikhan")

# function calling another function
def greet_all():
    greet()
    welcome("Samet")

greet_all()