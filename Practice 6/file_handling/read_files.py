# Exercise 1 - Create a file and write sample data
with open("students.txt", "w") as f:
    f.write("Alice   90\n")
    f.write("Bob     85\n")
    f.write("Charlie 92\n")
    f.write("Diana   78\n")
    f.write("Edward  88\n")
print("Exercise 1 - File created: students.txt")

# Exercise 2 - Read and print file contents
print("\nExercise 2 - Read the file")

# read()
print("\n-- read() --")
with open("students.txt", "r") as f:
    content = f.read()
print(content)

# readline()
print("-- readline() --")
with open("students.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
print("Line 1:", line1.strip())
print("Line 2:", line2.strip())

# readlines()
print("\n-- readlines() --")
with open("students.txt", "r") as f:
    lines = f.readlines()
print("All lines:", lines)
print("Total:", len(lines))
print("Last:", lines[-1].strip())

# looping over a file is the most memory-friendly way
print("\n-- loop over file --")
with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())