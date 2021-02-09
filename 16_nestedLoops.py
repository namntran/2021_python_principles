for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print()

for i in range(4):
    for j in range(5):
        print(i,j)

for i in range(0,3):
    for j in range(0,3):
        print(j, end=" ")
    print()

#triangle of 0
for i in range(0,7):
    for j in range (0,7-i): 
        print(" ", end="")
    for k in range(0, i + 1):
        print("0", end="")
    print("")

#pyramid of 0
for i in range(0,7):
    for j in range (0,7-i): 
        print(" ", end="")
    for k in range(0, 2*i+1):
        print("0", end="")
    print("")

#pyramid of 0
pyramidWidth = 10
for i in range(0,pyramidWidth):
    for j in range (0,pyramidWidth-i): 
        print(" ", end="")
    for k in range(0, 2*i+1):
        print("0", end="")
    print("")

#Number Pattern (Printing Numbers in Pyramid Shape)
num = int(input("enter the number of rows: "))
for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

 
# Python Program to Print Box Number Pattern of X and 0
 
rows = int(input("Please Enter the total Number of Rows  : "))
columns = int(input("Please Enter the total Number of Columns  : "))

print("Box Number Pattern of X and 0") 
 
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

print("Box Number Pattern of X and 0") 
 
for i in range(1, rows + 1):
    for j in range(1, columns - 1):
        if(i == 1 or i == rows or j == 1 or j == columns):          
            print('X', end = '  ')
        else:
            print('0', end = '  ')
    print()
