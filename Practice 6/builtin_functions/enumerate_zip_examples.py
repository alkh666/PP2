from itertools import zip_longest

names    = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
scores   = [90, 85, 92, 78, 88]
subjects = ["Math", "Physics", "Python", "Algebra", "History"]
hours    = [4.5, 2.0, 6.0, 3.5, 1.5]
# Exercise 3 - enumerate() and zip()

# enumerate() gives you index + value at the same time
print("\nenumerate(names):")
for i, name in enumerate(names, start=1):
    print(f"  {i}. {name}")

# without enumerate - the clunky old way
print("\nwithout enumerate:")
for i in range(len(names)):
    print(f"  {i}: {names[i]}", end="  ")

print("\n\nwith enumerate:")
for i, name in enumerate(names):
    print(f"  {i}: {name}", end="  ")
print()

# zip() pairs up two or more lists
print("\nzip(names, scores):")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# zip with three lists
print("\nzip(names, scores, subjects):")
for name, score, subject in zip(names, scores, subjects):
    print(f"  {name:<10} scored {score} in {subject}")

# build a dictionary from two lists
score_dict = dict(zip(names, scores))
print("\ndict(zip(names, scores)):")
print(" ", score_dict)

# zip stops at the shortest list
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]
print("\nzip stops at shortest:")
print(" ", list(zip(a, b)))

# zip_longest pads with a fill value instead
print("zip_longest fills missing with '?':")
print(" ", list(zip_longest(a, b, fillvalue="?")))

# combine enumerate and zip
print("\nenumerate + zip:")
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"  {i}. {name:<10} - {score} pts")

# Exercise 4 - Type checking and conversion

# type() tells you what type a value is
print("\ntype():")
values = [42, 3.14, "hello", True, None, [1, 2], (1, 2)]
for v in values:
    print(f"  {str(v):<15}  type: {type(v).__name__}")

# isinstance() checks if a value belongs to a type
print("\nisinstance():")
print("  isinstance(42, int)     :", isinstance(42, int))
print("  isinstance(3.14, float) :", isinstance(3.14, float))
print("  isinstance('hi', str)   :", isinstance("hi", str))
print("  isinstance(True, int)   :", isinstance(True, int))  # True! bool is a subclass of int
print("  isinstance(42, (int, float)) :", isinstance(42, (int, float)))  # check multiple types

# type conversion
print("\ntype conversion:")
print("  int('42')        =", int("42"))
print("  int(3.99)        =", int(3.99), "  <- truncates, not rounds!")
print("  float('3.14')    =", float("3.14"))
print("  str(100)         =", str(100))
print("  bool(0)          =", bool(0))
print("  bool(1)          =", bool(1))
print("  bool('')         =", bool(""))
print("  bool('hello')    =", bool("hello"))
print("  list('abc')      =", list("abc"))
print("  tuple([1,2,3])   =", tuple([1, 2, 3]))
print("  set([1,1,2,2,3]) =", set([1, 1, 2, 2, 3]))

# safe conversion - wrap in try/except to handle bad input
print("\nsafe int conversion:")

def safe_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None

test_vals = ["42", "3.14", "hello", None, "99", ""]
for v in test_vals:
    result = safe_int(v)
    print(f"  safe_int({str(v):<8}) = {result}")

# falsy values - these all equal False in a boolean context
print("\nfalsy values (all become False):")
falsy = [0, 0.0, "", [], {}, set(), None, False]
for v in falsy:
    print(f"  bool({str(v):<8}) = {bool(v)}")