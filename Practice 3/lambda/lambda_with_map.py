nums = [1, 2, 3, 4, 5]

# map to double numbers
doubled = list(map(lambda x: x*2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

# map to square numbers
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

# combine map with simple functions
incremented = list(map(lambda x: x+1, nums))
print(incremented)  # [2, 3, 4, 5, 6]