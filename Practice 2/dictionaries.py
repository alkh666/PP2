# example of dictionary
mydict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# dictionaries are ordered (Python 3.7+), changeable and do not allow duplicates
# we access values using keys

print(mydict["model"])

# change value
mydict["year"] = 2024

# add new key-value pair
mydict["color"] = "red"

# remove element
mydict.pop("brand")

# loop through dictionary
for key in mydict:
    print(key, mydict[key])

# dictionary methods

print(mydict.keys())    # returns keys
print(mydict.values()) # returns values
print(mydict.items())  # returns key-value pairs

# check if key exists
if "model" in mydict:
    print("model is in the dictionary")

# IN OTHER WORDS
# dictionaries store data in key : value pairs
# keys must be unique