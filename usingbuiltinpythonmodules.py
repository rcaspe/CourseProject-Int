# to see the comprehensive list of buil-in modules
'''help("modules")'''
# to view the specific attribute of a module 
# help ("module name")
'''help("random")'''

# display a random number
# import random module (it provide pseudo random numbers)

'''
from random import randint
print(int(randint(1,1000)))

'''

# datetime module provides classes which allow us to work with date and time.

'''import datetime

t = datetime.datetime.now()

print(t)
'''

# to format the date provided from datetime module
# we can use the strftime() method, which will make strings out of our imported date objects

import datetime

t = datetime.datetime(2021, 5, 17)

print(t.strftime("%B"))
# print the year
print(t.year)

# to use different ddate
x = datetime.datetime(1963, 8, 28)
print(x)

# to get access to python module index 
link = "https://docs.python.org/3/py-modindex.html"

# some of the modules and are built-in and other stored in external libraries
# lib (external libraries are accessible from pycharm)

# some modules don't come pre-installed in python
# using pip a python package manager that allows us to install different python modules

# to check if we have pip
'''
>> cmd
>> py -m pip --version
# check if anything comes up
# otherwise install pip


'''

# Reminders
# dir - returns a list of valid attributes of the object

