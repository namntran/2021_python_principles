# Python Program to Print sequence of numbers
 
print("Print numbers from user input using for loop and range") 
rows = int(input("Please enter the total range of numbers : "))

for i in range(1, rows + 1):
    print(i, end = ' ')          
print()

# Python Program to Print Box Number Pattern of X and 0
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box number pattern of X and 0") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('X', end = '  ')
        else:
            print('0', end = '  ')
    print()

# Python Program to Print Box Number of alternating Pattern of X and 0
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box number pattern of alternating X and 0") 
 
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if (i + j) % 2 == 0:
            print('X', end = ' ')          
        else:
            print('0', end = ' ')
    print()


# Python Program to Print Box Number of numbers
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box number pattern of numbers and rows") 
 
for i in range(1, rows + 1):
    print("row ", i, ":", end = " ")
    for j in range(1, columns + 1):
        print(j, end = " ")
    print()


# Python Program to Print Box Number of numbers
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box number pattern of numbers and rows") 
 
for i in range(1, rows + 1):
    # print("row ", i, ":", end = " ")
    for j in range(1, columns + 1):
        print(j, end = " ")
    print()

