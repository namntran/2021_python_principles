#program returns maximum and minimum values of given list

# print("List: ", list) #temp
quit = ""

while True: # sentinel pattern
    str = input("List: ") # accepts string inputs separated by a space
    list = str.split() # string method split() returns a list of strings resulting after cutting the initial string by spaces. 

    for i in range(len(list)): # convert each item to int type
        list[i] = int(list[i])

    if str == quit: # exit the loop
        break

    # print(list) #temp
    print ("List: ", len(list))
    print("min:", min(list), "max: ", max(list))
