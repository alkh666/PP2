def num():
    for i in range(n,-1,-1):
        yield i
n = int(input())
a = list(num())
print(*a)