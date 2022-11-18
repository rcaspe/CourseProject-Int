

class Customers:
    greeting = "Welcome to the Coffee Palace"
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Nate", "Espresso", "Food", 220)
c_2 = Customers("Elaine", "Strawberry Frappuccino", "Tuna Wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon Roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed Doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry Pancakes", 315)

print(Customers.greeting)

print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)

print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)