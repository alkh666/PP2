nums = [1, 2, 3, 4, 5, 6]

# filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

# filter numbers greater than 3
greater_than_3 = list(filter(lambda x: x > 3, nums))
print(greater_than_3)  # [4, 5, 6]

# combine map and filter
doubled_evens = list(map(lambda x: x*2, filter(lambda x: x % 2 == 0, nums)))
print(doubled_evens)  # [4, 8, 12]