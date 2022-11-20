rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

'''
In the above program, let's see how the pattern is printed.

    First, we get the height of the pyramid rows from the user.
    In the first loop, we iterate from i = 0 to i = rows.
    The second loop runs from j = 0 to i + 1. In each iteration of this loop, we print i + 1 number of * without a new line. Here, the row number gives the number of * required to be printed on that row. For example, in the 2nd row, we print two *. Similarly, in the 3rd row, we print three *.
    Once the inner loop ends, we print new line and start printing * in a new line.

'''

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

'''
In the above program, let's see how the pattern is printed.

    First, we get the height of the pyramid rows from the user.
    In the first loop, we iterate from i = 0 to i = rows.
    In the second loop, we print numbers starting from 1 to j, where j ranges from 0 to i.
    After each iteration of the first loop, we print a new line.

'''

rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")

'''
The working of the above example is also similar to the other examples discussed above except that the ascii values are printed here. The ascii value for alphabets start from 65 (i.e. A). Therefore, in each iteration, we increase the value of ascii_value and print its corresponding alphabet.

'''

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print("\n")

'''
This example is similar to an upright pyramid except that here we start from the total number of rows and in each iteration we decrease the number of rows by 1.
'''

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print("\n")

'''
The only difference between an upright and an inverted pyramid using numbers is that the first loop starts from the total number of rows to 0.
'''

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

'''
This type of pyramid is a bit more complicated than the ones we studied above.

    The outermost loop starts from i = 1 to i = row + 1.
    Among the two inner loops, the for loop prints the required spaces for each row using formula (rows-i)+1, where rows is the total number of rows and i is the current row number.
    The while loop prints the required number stars using formula 2 * i - 1. This formula gives the number of stars for each row, where row is i.

'''
rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

'''
Like example 6, this example also makes use of two loops inside a for loop.

    The outer for loop iterates through each row.
    Here we use two counters count and count1 for printing the spaces and numbers respectively.
    The inner for loop prints the required spaces using formula (rows-i)+1, where rows is the total number of rows and i is the current row number.
    The while loop prints the numbers where 2 * i - 1 gives the number of items in each row.

'''
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

'''
In this example, we have used a total of 4 for loops.

    The outer for loop iterates from i = rows to i = 1.
    The first inner for loop prints the spaces required in each row.
    The second inner for loop prints the first half of the pyramid (vertically cut), whereas the last inner for loop prints the other half.

'''

rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

'''
In this example, we have used three for loops.

    The outer loop iterates from 1 to rows + 1.
    The first inner loop prints the spaces.
    The second inner loop first finds the number to be printed using statement coef = coef * (i - j) // j and then prints it. Here, i is the row number and j is the value ranging from 0 to i.

'''

rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()

'''
This is one of the easiest patterns.

    number variable is initialized with value 1.
    The outer for loop iterates from 1 to the total number of rows.
    The inner for loop starts from 1 to i + 1, where i is the row number. After each iteration, the value of the number is increased.

'''
