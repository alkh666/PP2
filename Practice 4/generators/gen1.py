def get_square():
    for i in range(1,n+1):
        yield i**2
n = int(input())
a = get_square()
print(*list(a))