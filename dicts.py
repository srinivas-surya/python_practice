
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}

print(thisdict)

# access the dictionaries
print("access the dict: ", thisdict["year"])

print("access the dict: ", thisdict.get("model"))

# change the values in dict
thisdict["year"] = 2000

print("updated dict: ", thisdict)

# adding the values in dict
thisdict["name"] = "srini"
print("updated dict: ", thisdict)

# print only values
print("print only values: ", thisdict.values())

# print only the keys

print("only keys: ", thisdict.keys())


# remove the item

# thisdict.pop("model")

print("remove the items: ", thisdict)

# clear the dict
# thisdict.clear()

# items function in dict
print("items : ", thisdict.items())

# from keys function

list1 = [1, 2, 1, 2, 3, 4]

thisdicts = list(dict.fromkeys(list1))

print(thisdicts)

# access the list of dicts

print("=================== list of dicts ======================")

new_dict = [{
    "brand": "ford",
    "model": "mustang",
    "year": 1964},
    {
        "brand": "maruti",
        "model": "swift",
        "year": 2000
    },
    {
        "brand": "Nano",
        "model": "TATA",
        "year": 2004
    }
]
brand_list = []
model_list = []

for i in new_dict:
    for key, value in i.items():
        print(key, ":", value)
        if key == "brand":
            brand_list.append(value)
        elif key == "model":
            model_list.append(value)


print("brand_list ", brand_list)
print("model_list: ", model_list)

print("============== access the values ====================")
# access the values in list

for i in new_dict:
    values = i.values()
    for j in values:
        print("values:", j)

print("============= access only the keys ===================")

for i in new_dict:
    keys = i.keys()
    for key in keys:
        print("key: ", key)
        
        
print("============= access nested dicts ====================")

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print(D['emp1']['name'])
# Prints Bob

print(D['emp2']['job'])
# prints Dev

# looping throgh the nested dicts

D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])
        
# adding new key-pair to the dicts
D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp4'] = {'name': 'Max', 'job': 'Janitor'}

print(D)
