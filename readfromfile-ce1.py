import os

'''f = open("readfromfile.txt", "x")
f.write("This is for coding challenge! 1 \n")
f.write("This is for coding challenge! 2 \n")
f.write("This is for coding challenge! 3 \n")

f = open("readfromfile.txt", "r")
print(f.read())

# use readline to get/read only single line
f = open("readfromfile.txt", "r")
print(f.readline())

# use the for loops
for x in f:
    print(x)'''

# remove the file

if os.path.exists("readfromfile.txt"):
    os.remove("readfromline.txt")
else:
    print("the file doesn't exists")