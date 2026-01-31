# Example of the list
lst = ["apple", "banana", "cherry"]
#list items are ordered, changeable, and allow duplicate values

lst = ["apple", "banana", "cherry", "apple", "cherry"]
print(lst)

l = ["apple", "banana", "cherry"]
print(len(l)) # length of the list

# List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# and can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# Access items
# List items are indexed and you can access them by referring to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# and you can change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# to add items to the list we can use different methods
# append() to add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# insert() method inserts an item at the specified index

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# extend() to append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#removing list items

#remove() method removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# loop through list
thislist = ["apple", "banana", "cherry"]
for item in thislist:
    print(item)

# sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sort descending
thislist = ["apple", "banana", "cherry"]
thislist.sort(reverse=True)
print(thislist)

# all list methods
"""
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
