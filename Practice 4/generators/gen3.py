def func():
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
n = int(input())
b = get_even()
for i in list(b):
    print(i,end = ',')