# default parameters
def power(number, exponent=2):
    return number ** exponent

print(power(5))      # 25
print(power(2, 3))   # 8

def greet(name="Friend", age=18):
    print(f"Hello {name}, age {age}!")

greet()
greet("Alikhan", 20)