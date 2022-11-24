# modules allow users to organize and reuse codes by importing prewritten files. "Within these modules are variables, functions, classes, etc. that you can import into a project"

# incorporate the module1.py to this program, use the module keyword
# import (name of the module to incorporate)
'''import module1 '''
# can use an allias when importing a module
'''import module1 as m1'''
# another way to import a module
# "from" keyword
# use import then asterist to get all the data from the module
'''from module1 import *'''
# to get specific function from the module
from module1 import get_diff

# create a module
'''
f = open("module1.py", "x")

'''
# use the greeting function from module1.py
'''module1.greeting("Stacy")'''

'''a = module1.user_1
print("Hey there, " + a.name + "! Ready to do some math?")
c = module1.user_3
print("Hey there, " + c.name + "! Ready to do some math?")'''

# RENAMING MODULES
'''a = m1.user_1
print("Hey there, " + a.name + "! Ready to do some math?")'''

# use other function
# when defining a function, we also use the return statement
# it sends the function results back to the caller
'''sum = m1.get_sum(4591, 782)
print(sum)

quotient = m1.get_quo(100, 22)
print(quotient)
'''

# another way to import a module
# "from" keyword
'''product = get_prod(9, 4)
print(product)'''

# to get specific function from the module
difference = get_diff(296, 57)
print(difference)