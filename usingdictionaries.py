# find specific data within dictionary
exam_scores = {"jonathan": 85, "erica": 99, "rose": 83, "henry": 92, "missy": 77, "ashleigh": 88, "paul": 60, "gordon": 86, "lisa": 90, "kelly": 77, "joe": 65, "tiffany": 67, "wesley": 97, "gail": 71}
# syntax: print(dictionary[key])
print(exam_scores["paul"])

# keyerrors - it occurs when you input a key that isn't actually present in the code
# create conditional statement that will check if the record that is trying to get is existing in the list or not without getting keyerrors

check_key = "andrey"

if check_key in exam_scores:
    print(check_key, " took the test")
else:
    print(check_key, " didn't took the test")

# quick way to know if the keys, exist or not
# use .get() method to retrieve information
# it will show the key we are looking for and returns none it if doesn't exist

# this two exist in the list
print(exam_scores.get("lisa"))
print(exam_scores.get("wesley"))
# this one doesn't exist in the list
print(exam_scores.get("queenie"))

# to delete a key in the dictionary
# use .pop() method

neighbors = {"ms. santos": "fruitcake", "mr. reyes": "cookies",
            "mrs. dela cruz": "cupcakes", "mr. tiu": "gingerbread man"}

print(neighbors)
# to delete a key to the dictionary use .pop() method
# example: removing one key in the list that already received their treats
done = neighbors.pop("mr. reyes")
print(neighbors)
# to get the keys only without their values use .keys() method
y = neighbors.keys()
print(y)
# to get all the values only without their keys use .values() method
x = neighbors.values()
print(x)
# to get both the keys and values use .items() method
z = neighbors.items()
print(z)