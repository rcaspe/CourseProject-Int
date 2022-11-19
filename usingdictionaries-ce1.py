
# I use this instead of groceries = {'chicken': 8, 'apples': 6, 'cucumbers': 3, 'milk': 2, 'oranges': 4}
items = ["chicken", "apples", "cucumbers", "milk", "oranges"]
units = [8, 6, 3, 2, 4]

# combine the 2 lists
groceries = dict(zip(items, units))
# the print output should be {'chicken': 8, 'apples': 6, 'cucumbers': 3, 'milk': 2, 'oranges': 4}
print(groceries)

# to remove specific information within the list
remove_items = groceries.pop("oranges")
print(groceries)

# create another list for speakers and their age
names = ["sir rafael", "ms. joan", "mrs. dana"]
ages = [54, 33, 67]

speakers = dict(zip(names, ages))
print(speakers)

# to get only the names of the speakers
z = speakers.keys()
print(z)

names = ["carl", "quentin", "john y.", "peter", "max t.", "joseph", "jone", "jorge", "george", "ben", "jerome", "rick", "max g", "john p.", "vince"]
results = ["passed", "failed", "passed", "failed", "passed", "passed", "failed", "failed", "passed", "passed", "passed", "failed", "failed", "failed", "passed"]

tryout = dict(zip(names, results))
y = tryout.get("jorge")
print(y)



