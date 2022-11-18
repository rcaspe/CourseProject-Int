# inheritance 
# allows classes to have code reusability within programming
# creating subclass from parent class 

# create class of the users
# this are the based or parent class
class User:
    # create instance variable
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def display(self):
        print("(parent class/User) Username: ", self.username, "password: ", self.password)

# create sub-class or child class
# this will inherit on based class
class Admin(User):
    def display2(self):
        print("(subclass/Admin) Username: ", self.username, "password: ", self.password)

# create variable for both user and admin
a_1 = Admin("leslie2001", "password1234")
u_45 = User("pretty_jun25", "otherpassword287")

# display the user list
# variable.method_name()
a_1.display2()
u_45.display()



# Overriding methods --------
# used to change what the mthod does. Within the subclass, we redefine the method (with the same name) to perform the task differently

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Parent class/user")
        print("Username: ", self.username)
        print("Password: ", self.password)

class Admin(User):
    # the method will be over-written through here
    # __init__ method of Admin subclass overrides __init__ method of User base class
    def __init__(self, username, password, code):
        self.code = code
        User.__init__(self, username, password)

    def display3(self):
        print("Subclass/Admin")
        print("Username: ", self.username)
        print("Password: ", self.password)
        print("Code: ", self.code)

u_45 = User("pretty_jun25", "otherpassword287")
a_1 = Admin("leslie2001", "password1234", "2468")

u_45.display()
a_1.display3()


# using super method
# is a method that allows you to call a method from the parent class
# use super method to get access to method and properties of a subclass
# the super method returns an object that represents the based class

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Parent class/user")
        print("Username: ", self.username)
        print("Password: ", self.password)

class Admin(User):
    def __init__(self, username, password, code):
        self.code = code
        super().__init__(username, password)

    def display3(self):
        super().display1()
        print("Code: ", self.code)

a_1 = Admin("leslie2001", "password1234", 2448)
a_1.display3()



