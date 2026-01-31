# boolean values
print(10 > 9) # returns True
print(10 == 9) # returns False
print(10 < 9) # returns False

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# returns b is not greater than a

# evaluate values and variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))
"""
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
# check if an object is an integer or not
x = 200
print(isinstance(x, int))