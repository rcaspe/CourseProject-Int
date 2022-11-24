'''f = open("functionfile.py", "x")
f.write("# this is connected to the modules-ce1.py")'''

from functionfile import greeting1
from functionfile import greeting2

a = greeting1()
print(a)
b = greeting2()
print(b)