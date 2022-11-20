# exception is use to manage error that arise during a program execution
# traceback which tells you where you made a blunder in your code

# raise keyword

# let us define errors and text that will be printed on the console when specified error occurs

# example: shoudn't accept negative value

'''n = -5
if n < 5:
    raise Exception("No negative value allowed!")'''

# syntax error
# systax errors occurs when the code is not written correctly

# assertions

'''employee_of_the_year = "roger"
x = employee_of_the_year

assert x == "roger"
assert x == "suzanne"'''

# dividing by zero leads to ZeroDivisionError
# it occurs when dividing by zero
'''
1/0'''

# TypeError 
# it occurs when an operation is performed on an incorrect or unsupported object type

'''50 ** "two"'''


# to handle different type of exception
# try and except - these blocks are used to spot and handle exception

# using try = we can test our code using try block to ensure that there are no errors
# if we encounter an except error it need to handle by the except block if not, the program will crash. It tells the program on how to respond to the exceptions.
# finally block - the finally block allows us to run our code no matter what the result of the try and except block

'''print(random-variable)'''

# use try and except block

'''try:
    print(random-variable)
except:
    print("exception alert!")'''

# you can defice as many exception blocks as you want for any type or error you may encounter

'''try:
    print(x + "macarons")
except NameError:
    print("please define your variable")
except IndentationError:
    print("please be careful when indenting your code.")
except:
    print("something else went wrong! we need to figure it out")
'''

# we can also use else keyword

'''try:
    print(599+343)
except:
    print("this operation cannot be performed")
else:
    print("no issues here")'''

# the finally block will run our code even if there are errors

try:
    print(h)
except:
    print("there's something wrong with our program")
finally:
    print("lets run our program anyways")