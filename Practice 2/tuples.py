# example of tuple
mytuple = ("apple", "banana", "cherry")

# tuple also has the following properties of list
# to access to elements of tuple we use indexing like in lists
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# tuples are unchangeable, to change elements of tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # not like in lists

# to add elements, we also use another method
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# to remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# in other words tuples are
# unchangeable, to change elements in tuple
# we convert it into lists,then change,
# finally convert it into tuple again

# UNPACK TUPLES
# unpacking means assigning tuple elements to variables

thistuple = ("apple", "banana", "cherry")
(a, b, c) = thistuple
print(a, b, c)

# LOOP TUPLES
# we can loop through a tuple using a for loop

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# JOIN TUPLES
# to join tuples, we use the + operator

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# TUPLE METHODS
# tuples have only two built-in methods

thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple.count("apple"))  # counts elements
print(thistuple.index("banana")) # finds index