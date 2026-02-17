# simple lambda functions
square = lambda x: x**2
add = lambda a, b: a + b
triple = lambda x: x*3

print(square(5))  # 25
print(add(3, 4))  # 7
print(triple(2))  # 6

# lambda with conditional
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(5))  # Odd
print(even_or_odd(6))  # Even