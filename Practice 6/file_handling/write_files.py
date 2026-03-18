import os
# Exercise 3 - Append new lines and verify content

# First create the file
with open("students.txt", "w") as f:
    f.write("Alice   90\n")
    f.write("Bob     85\n")
    f.write("Charlie 92\n")

print("Exercise 3 - File before appending:")
with open("students.txt", "r") as f:
    print(f.read())

# "a" mode adds to the end without erasing existing content
with open("students.txt", "a") as f:
    f.write("Diana   78\n")
    f.write("Edward  88\n")

print("File after appending:")
with open("students.txt", "r") as f:
    print(f.read())

# verify by counting lines
with open("students.txt", "r") as f:
    lines = f.readlines()
print("Total lines now:", len(lines))

# writelines() - write a list of strings at once
print("-- writelines() --")
items = ["apple\n", "banana\n", "cherry\n"]
with open("fruits.txt", "w") as f:
    f.writelines(items)

with open("fruits.txt", "r") as f:
    print(f.read())

# mode "x" - create only if file does NOT exist
print("-- mode x (exclusive create) --")
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")

with open("newfile.txt", "x") as f:
    f.write("Created fresh.\n")
print("newfile.txt created.")

try:
    with open("newfile.txt", "x") as f:
        f.write("Try again.")
except FileExistsError:
    print("Error: newfile.txt already exists.")

# Clean up
for name in ["students.txt", "fruits.txt", "newfile.txt"]:
    if os.path.exists(name):
        os.remove(name)