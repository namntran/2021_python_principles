# 12_marks.py
# Prompt for and read marks for a test unit a negative number is entered.
# Print the number of marks entered and the average (arithmetic mean) of marks
# Print the  highest and lowest marks
# use indefinite loop - while loop

n = 0
total = 0.0
mark = float(input("Enter a mark: ")) #initialise variables to the first value  it  should have, don't make up numbers
highest = mark #initialise variables to the first value  it  should have, don't make up numbers
lowest = mark #initialise variables to the first value  it  should have, don't make up numbers
while mark >= 0.0:
    n += 1 
    total += mark
    if mark > highest:
            highest = mark
    if mark < lowest:
            lowest = mark
    mark = float(input("Enter a mark: "))
print("The number of marks: ", n)
if n > 0: # only print average if n > 0
    print("The average mark is: ", total/ n)
    print("The lowest mark is: ", lowest)
    print("The highest mark is: ", highest)

