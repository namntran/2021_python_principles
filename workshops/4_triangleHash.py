# Program that prints a triangle of hashes using nested for loop

num = int(input("enter the number of rows: "))
for i in range(0,num+1):
    for j in range (0,num-i): 
        print(" ", end="") #print blank space of each row
    for k in range(0, 2*i+1):
        print("#", end="")
    print("")
