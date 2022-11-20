
# use raise exception
'''x = 500
if x > 100:
    raise Exception("x should not be bigger than 100")'''

# use try and except block

'''try:
    print(variable_1)
except:
    print("exception alert")'''

# run the code even there's an error

'''for i in range(6):
    print("im so happy")'''

# else keyword

'''try:
    print(12*6)
except:
    print("this operation cannot be performed")
else:
    print("no issues here")
'''

# to get an assertion error

best_burger = "Burger King"
x = best_burger
number_2_burger = "McDonalds"
y = number_2_burger

assert x == "eks"
assert y == "way"
