# program to calculate the max and min length

while True:  # sentinel pattern: while loop 
    print("Find the length and width of room from user input") 
    a = float(input('Enter room dimension 1 (m): '))
    b = float(input('Enter room dimension 2 (m): '))
    length = max(a,b) #max return highest iterable item
    width = min(a,b)

    if a <= 0 or b <= 0:  # exit loop if user entered zero or minus
        break

    print("length: ", length, "m and width: ", width, "m")  # print length and width using max and min function
    print() # print new line