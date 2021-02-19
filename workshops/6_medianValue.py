# program to calculate median value

import statistics # to call median module. Return the median (middle value) of numeric data, using the common “mean of middle two” method.

listNum = [] # create an empty list to store numbers

while True:
    num = input("Enter a number: ") # user enters input of strings   
    if num  == "": # exit the loop
        break
    else:
        listNum.append(int(num)) # adding the element to the empty list

total = sum(listNum)
avg = total/len(listNum)
median = statistics.median(listNum)

print("Numbers entered in ascending order: ", sorted(listNum)) #prints the list of sorted numbers
print ("Items in list: ", len(listNum))
print(f'Total of numbers: {total}, Average of numbers: {avg}') 
print(f'Median: {median}')