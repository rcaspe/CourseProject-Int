# looping through dictionaries
i = ["name", "position", "email address"]
a = ["frank", "sales representative", "frank@company.com"]

employee_1 = dict(zip(i, a))

# for statement to loop through the data
for key, value in employee_1.items():
    print(key)
    print(value)

c = ["harry potter", "percy jackson", "katniss everdeen", "bilbo baggins"]
w = ["want", "riptide", "bow and arrow", "ring"]

# loop through the dictionary and get only the keys
character_weapons = dict(zip(c, w))
for name in character_weapons.keys():
    print(name)

# use continue statement in the dictionary
# loop through the keys
for name in character_weapons.keys():
    if name == "percy jackson":
        continue
    print(name)

# use .values() method and loop through dictionary
# personal remarks: didn't try to join using (dict(zip)) with 1 key and 2 values (will try next time)
most_delicious = {"mcdonald's": ["fried chickens", "sundae"], "jollibee": ["fried chicken", "spaghetti"],
                    "kfc": ["gravy", "mashed potatoes"], "pizza hut": ["pizza", "pasta"]} 
# only the food items will be print the in console
x = most_delicious
# loop through values
for item in x.values():
    # print the value of item
    print(item)

# nested keyword with dictionary
# creating a dictionary within a dictionary
cat = {
    1: {"name": "sweetie", "age": "12", "color": "white"},
    2: {"name": "ethel", "age": "3", "color": "orange"}
    }
print(cat)
# to access the elements of the each dictionaries use []
print(cat[2]["age"])
print(cat[1]["name"])
print(cat[2]["color"])
# using empty {} we can create a new dictionary
# add new dictionary
cat[3] = {}
cat[3]["name"] = "tuna"
cat[3]["age"] = "5"
cat[3]["color"] = "black"
cat[3]["personality"] = "friendly"

print(cat[1])
print(cat[2])
print(cat[3])

# another way to add new dictionary
cat[4] = {"name": "bubbles", "age": "7", "color": "gray", "personality": "grumpy"}

print(cat[1])
print(cat[2])
print(cat[3])
print(cat[4])

