
# create two list
flavor = ["vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]

# merge two lists
ice_cream = dict(zip(flavor, toppings))
print(ice_cream)

# overwrite the existing key value of the lists
ice_cream["chocolate"] = "blueberry"
print(ice_cream)

# update the current list (additional key value)
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)