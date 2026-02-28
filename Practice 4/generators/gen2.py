def get_even():
    for i in range(n):
        if i%2==0:
            yield i
n = int(input())
b = get_even()
for i in list(b):
    print(i,end = ',')