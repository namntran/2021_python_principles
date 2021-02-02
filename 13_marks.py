# 13_marks.py
# Prompt for the number of marks and read them.
# Print the number of marks entered and the average (arithmetic mean) of marks
# Print the  highest and lowest marks
# use definite loop - for loop

n = int(input("How many marks to be entered: "))
if n > 0: # only print average if n > 0
    mark = float(input("Enter a mark: ")) 
    highest = mark 
    lowest = mark 
    total = mark
    for i in range(n - 1):
        mark = float(input("Enter a mark: ")) 
        total += mark
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    print("The number of marks: ", n)
    print("The average mark is: ", total/ n)
    print("The lowest mark is: ", lowest)
    print("The highest mark is: ", highest)