# example of match case (Python 3.10+)

x = "apple"
match x:
    case "apple":
        print("This is an apple")
    case "banana":
        print("This is a banana")
    case _:
        print("Unknown fruit")

# match can check multiple values in one case
y = 2
match y:
    case 1 | 2 | 3:
        print("y is 1, 2, or 3")
    case _:
        print("y is something else")

# match with patterns and variables
point = (0, 0)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On X axis at {x}")
    case (0, y):
        print(f"On Y axis at {y}")
    case _:
        print("Somewhere else")

# IN OTHER WORDS
# match replaces multiple if/elif conditions
# case _ is like else (default)