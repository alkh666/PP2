# example of while loop
i = 1
# while loop runs while condition is True
while i <= 5:
    print(i)
    i += 1

# while with break
x = 0
while True:
    if x == 3:
        break
    print(x)
    x += 1

# while with continue
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue
    print(y)

# while with else
z = 0
while z < 3:
    print(z)
    z += 1
else:
    print("loop finished")

# IN OTHER WORDS
# while repeats code while condition is True
# break stops the loop
# continue skips current iteration
# else runs when loop finishes normally