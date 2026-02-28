def squares():
    for i in range(a,b+1):
        yield i**2
a = int(input())
b = int(input())
c = list(squares())
print(*c)