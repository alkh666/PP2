from functools import reduce
scores = [72, 88, 91, 45, 63, 95, 80, 57, 76, 84]
names  = ["Alice", "Bob", "Charlie", "Diana", "Edward",
          "Frank", "Grace", "Henry",  "Irene", "Jack"]
prices = [1200, 450, 3500, 890, 2100, 670, 4200]

# Exercise 1 - map() and filter()

# map() applies a function to every item in a list
def to_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

grades = list(map(to_grade, scores))
print("\nscores:", scores)
print("grades:", grades)

# apply 10% discount to all prices
discounted = list(map(lambda p: round(p * 0.9), prices))
print("\noriginal prices:", prices)
print("discounted (10%):", discounted)

# convert a list of strings to integers
raw = ["10", "25", "38", "47"]
nums = list(map(int, raw))
print("\nstrings:", raw)
print("integers:", nums)

# filter() keeps only items that pass the test
passed = list(filter(lambda s: s >= 60, scores))
failed = list(filter(lambda s: s < 60, scores))
print("\npassed (>=60):", passed)
print("failed  (<60):", failed)

# filter() with None removes all falsy values
dirty = [1, None, "hello", "", 0, "world", False, 42]
clean = list(filter(None, dirty))
print("\nbefore:", dirty)
print("after filter(None):", clean)

# map + filter together: names of top students
top = list(map(lambda p: p[0],
               filter(lambda p: p[1] >= 90, zip(names, scores))))
print("\ntop students (score >= 90):", top)

# Exercise 2 - reduce()

# reduce() collapses a list into one value
# reduce(f, [a, b, c]) -> f(f(a, b), c)

total = reduce(lambda acc, x: acc + x, scores)
print("\nsum via reduce:", total)
print("average:", round(total / len(scores), 1))

# step-by-step demo: multiply 1 * 2 * 3 * 4 * 5
print("\nstep-by-step: 1 * 2 * 3 * 4 * 5")

def multiply_and_show(acc, x):
    result = acc * x
    print(f"  {acc} x {x} = {result}")
    return result

product = reduce(multiply_and_show, [1, 2, 3, 4, 5])
print("result:", product)

# reduce with a starting value (third argument)
result = reduce(lambda acc, x: acc + x, [10, 20, 30], 100)
print("\nreduce(sum, [10,20,30], start=100):", result)

# find max without max()
biggest = reduce(lambda a, b: a if a > b else b, scores)
print("max score without max():", biggest)