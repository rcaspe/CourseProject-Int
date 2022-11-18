# init method
# is a constructor in object oriented concepts. Its used to assign values to object properties, or other operations that are necessary when the object is being created
# object oriented programming is a method or approach of organizing a program by grouping properties, methods, and atrributes into individual objects
# objects are data structure that are definced by its class, comprised of methods, class variables, and instance variables
# attributes are data stored inside a class or instance that represent the state of the class or instance
# methods are a type of function that is defince in a class

# create class "Guest"
class Guest:
    # self is the instance of our class
    # create instance variable to input info needed
    # __init__ method is used to assgin values to the properties and operations of objects when it is being created.
    def __init_(self, first, last, interest, phone):
        # instance variable
        # can use it to access attributes and methods
        self.first = first
        self.last = last
        self.interest = interest
        self.phone = phone

# add data into Guest
# variable = class_name ("attributes")
g_1 = Guest("Eve", "Dela Cruz", "Anime", 12345)
g_2 = Guest("Adam", "Perez", "Russian literature", 87654)

# get the specific data
# print(variable_name.variable_value)
print(g_1.last)
print(g_2.phone)

# add data into Guest
# variable = class_name ("attributes")
g_3 = Guest("Mike", "Lim", "Movies", 59821)
g_4 = Guest("Katie", "Lopez", "Sports", 81901)
g_5 = Guest("Bert", "Smith", "Cooking", 19027)

# get the specific data
# print(variable_name.variable_value)
print(g_3.phone)
print(g_4.interest)
print(g_5.last)
