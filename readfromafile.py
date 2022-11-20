'''
# file more r will return the whole text / content of the file
f = open("python question", "r")
print(f.read())

# to read only the specific content of a file
# to return only character
print(f.read(12))

# to return a single line
print(f.readline())
print(f.readline())
print(f.readline())

# using for loop to read the whole file line by line
for x in f:
    print(x)

# must close the file every use
f.close()
'''
# to delete a file

# to delete a file that could not be exist
import os

if os.path.exists("todelete.txt"):
    os.remove("todelete.txt")
else:
    print("the file doesn't exist")

# to delete a file that surely exist

import os
os.remove("todelete")