# list

fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print("fruits: ", fruitList)

# accessing the list
print("list accessing: ", fruitList[0])

# Range indexing
print("range indexing: ", fruitList[2:4])

# negative indexing
print("negative indexing: ", fruitList[-4:-1])

# change the items in list
fruit = ["apple", "banana", "cherry"]
fruit[1] = "mango"
print("new list :", fruit)

print("====================list built in methods ============================================")

# append item to list

fruit.append("mango")
print("append list : ", fruit)

# insert item to list
fruit.insert(1, "orange")
print("insert list: ", fruit)

# remove item in list

# fruit.remove("banana")
print("remove item from list :", fruit)

# pop item in list
# fruit.pop(1)
print("pop item from list:", fruit)

# use del keyword to remove to item or list

# del fruit[0]

print("del keyword list :", fruit)

# clear the list

# fruit.clear()

print("clear list :", fruit)

# copy list
copyList = fruit.copy()
print("copyList: ", copyList)

# join list

joinList = [1, 2, 3, 4, 5]
newList = fruit + joinList
print("new joined list :", newList)

# extend the list
fruitList.extend(joinList)
print("extend List: ", fruitList)

# count of the list
print("count of the list : ", fruitList.count(2))

# reverse the list
fruitList.reverse()
print("reverse list:", fruitList)

# sort list
fruits_list = ["apple", "mango", "banana"]
fruits_list.sort()
print("sortedList: ", fruits_list)

print("=======list of lists============================")

list_of_list = [["apple", "ball", "cat"], [1, 2, 3, 4], ["red", "blue", "yellow"]]

# access element by element
for i in list_of_list:
    print("element by element: ", i[0], i[1], i[2])


# check the element in the list
for i in list_of_list:
    for j in i:
        if j == 1:
            print("element present in list")
            break

# prepare list with data 
new_list = []

for i in range(0, 10):
    new_list.append(i)
    
print(new_list)


# print list of list

L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for list in L:
    for number in list:
        print(number, end=' ')

