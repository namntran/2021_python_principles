def is_arithmetic(list):
    
    diff = list[1] - list[0] # calculating the difference between the first two elements of the sequence 
    for index in range(len(list) - 1):# is difference constant throughout the list by iterating over each element of the list 
        if not (list[index + 1] - list[index] == diff):
            return False
    return True #if difference evaluates to true the given list is in arithmetic progression.

quit = ""

while True: # sentinel pattern
    list = input("List: ")
    list = list.split() # string method split() returns a list of strings resulting after cutting the initial string by spaces. 

    for i in range(len(list)): # convert each element to int type
        list[i] = int(list[i])

    if str == quit:  # exit the loop
        break

    print(is_arithmetic(list))


