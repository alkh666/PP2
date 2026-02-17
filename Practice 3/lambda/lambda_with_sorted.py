words = ["banana", "apple", "cherry", "date"]

# sort by length
sorted_by_len = sorted(words, key=lambda x: len(x))
print(sorted_by_len)  # ['date', 'apple', 'banana', 'cherry']

# sort alphabetically
sorted_alpha = sorted(words, key=lambda x: x)
print(sorted_alpha)  # ['apple', 'banana', 'cherry', 'date']

# sort by last character
sorted_last_char = sorted(words, key=lambda x: x[-1])
print(sorted_last_char)  # ['banana', 'apple', 'date', 'cherry']