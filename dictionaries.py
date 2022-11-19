# dictionaries contain a set of key-value pairs.
# A key-value pair is a set of values associated with each other.

# dictionary is a collection of unordered data, which is stored in key-value pairs
# the key is a unique identifier for some item of data

# dictionary syntax
# dictionary_name = {key: value, key: value, key: value} 
# dictionary_name = elements of the dictionary
shopping_list = {"weird hat": 150, "purple rug": 450, "old books": 200, "stuffed elephant": 50}

print(shopping_list)

# list values
basketball_teams = {"Crouching Tigers": ["Jacob", "Kevin", "Roni", "Joshua", "Isagani"], "Hidden Dragons": ["Ted", "Bryan", "Edu", "Luis", "Mark"]}

print(basketball_teams)

# use different data types as values
anime_character = {"Name": "Eren", "Age": 19, "Childhood Friends": ["Armin", "Mikasa"]}

print(anime_character)

# REMINDER:
# While dictories and list can be use as values, they CANNOT be use as KEYS

# add new key to the dictionaries
shopping_list = {"weird hat": 150, "purple rug": 450, "old books": 200, "stuffed elephant": 50}
# syntax: dictionary[key] = value
shopping_list["Plastic Ring"] = 20
# to override existing keys
shopping_list["stuffed elephant"] = 80

print(shopping_list)

# to add more than 1 item to the dictionary

pets = {"Geral": "guinea pig", "Alice": "dog", "Ruby": "car"}
# syntax: dictionary_name.update({key:value,key:value})
pets.update({"Ront": "gecko", "Paulina": "hamster", "Marlon": "goldfish"})

print(pets)

# combine 2 list and turn then into one dictionary
# zip function: take two or more lists and combines them
# dict function: turns the combines list into a dictionary

# 1st list
relative = ["Tita Malou", "Jeff", "Tito Roger", "Veronica"]
# 2nd list
age = [54, 14, 55, 19]

# combine the list using zip function
combined_list = zip(relative, age)
print(list(combined_list))

# combine (and format) the list using dict function
relative_age = dict(zip(relative, age))
print(relative_age)