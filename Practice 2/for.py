# example of for loop
# for loop iterates over a sequence
for i in range(1, 6):
    print(i)

# for with break
for x in range(5):
    if x == 3:
        break
    print(x)

# for with continue
for y in range(1, 6):
    if y == 3:
        continue
    print(y)

# for with else
for z in range(3):
    print(z)
else:
    print("loop finished")

# loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# IN OTHER WORDS
# for iterates over a sequence (list, tuple, set, string, range)
# break stops the loop
# continue skips current iteration
# else runs when loop finishes normally