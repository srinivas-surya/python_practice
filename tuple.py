myTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Access the tuple
print(myTuple[0])

# range index in tuple

print("range tuple: ", myTuple[0:5])

# negative tuple

print("negative tuple : ", myTuple[-4:])

# change tuple values

newTuple = list(myTuple)
newTuple[1] = "mango"
myTuple = tuple(newTuple)
print("new tuple: ", myTuple)

# len of the tuple

print(len(myTuple))

# create tuple with one item we have to add comma or it consider as another data type

# delete keyword

# del myTuple

# count of the items in tuple
print("count: ", myTuple.count("apple"))

# index of the items in tuple

print("index: ", myTuple.index("apple"))

# count function
print("count: ", myTuple.count("apple"))

# list of tuples
print("=============== access the list of tuples ==============")
list_tuples = [("car", "bike", "train"), ("honda", "hero", "bajaj"), ("mango", "apple", "grape")]

for i in list_tuples:
    print("list of tuples:", i[0], i[1], i[2])

print("=========== unpacking =========================")

# tuple unpacking

for i, j, k in list_tuples:
    print("unpacking: ", i, j, k)


