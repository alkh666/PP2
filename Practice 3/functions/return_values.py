# return values
def square(x):
    return x ** 2

def sum_two(a, b):
    return a + b

result1 = square(5)
result2 = sum_two(3, 4)

print(result1)  # 25
print(result2)  # 7

# returning multiple values
def arithmetic(a, b):
    return a+b, a-b, a*b, a/b

add, sub, mul, div = arithmetic(10, 2)
print(add, sub, mul, div)