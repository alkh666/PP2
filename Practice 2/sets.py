# example of set
myset = {"apple", "banana", "cherry"}

# sets are unordered and unindexed
# we cannot access elements by index

myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)

# sets do not allow duplicate values

thisset = {"apple", "banana", "apple"}
print(thisset)

# sets are changeable
# we can add elements to a set

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# to add multiple elements, we use update()

thisset = {"apple", "banana", "cherry"}
thisset.update(["mango", "grape"])
print(thisset)

# to remove elements from a set

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")   # gives error if element not found
# thisset.discard("banana")  # no error if element not found
print(thisset)

# JOIN SETS
# we can join sets using union() or update()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# SET METHODS
# some common set methods

thisset = {"apple", "banana", "cherry"}
print("apple" in thisset)   # check existence
print(len(thisset))         # length of set

# IN OTHER WORDS
# sets are unordered and unindexed
# sets do not allow duplicate elements
# sets are changeable (mutable)