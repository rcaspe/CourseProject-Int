
# binary file - are used for storing media files, compiled code, or app data
# text file - are readable to us (ex plain text or source code)

# open() function parameters
# syntax = open(filename, mode)
# type of mode when opening a file
# (r)read, (a)append, (w)write, (x)create

# create
'''f = open("newfile.txt", "x")'''

# write and read file
# using w will overwrites existing content of the file
f = open("newfile.txt", "w")
f.write("i am sure of it!")

# to read the content of the file
f = open("newfile.txt", "r")
print(f.read())
f.close()

# to add something into the file use append
f = open("newfile.txt", "a")
f.write("\npython intermediate")

f = open("newfile.txt", "r")
print(f.read())
