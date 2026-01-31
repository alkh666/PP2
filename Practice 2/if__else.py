# example of if else

a = 10
b = 5

# if checks a condition
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# if elif else example

x = 0

if x > 0:
    print("positive number")
elif x < 0:
    print("negative number")
else:
    print("zero")

# nested if example

age = 18

if age >= 18:
    if age < 65:
        print("adult")
    else:
        print("senior")
else:
    print("child")

# IN OTHER WORDS
# if executes code when condition is True
# else executes code when condition is False
# elif checks another condition