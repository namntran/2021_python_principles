# program that returns the common elements of set and list
# not part of workshop problems

quit = ""

while True: # sentinel pattern
    str1 = input("List 1: ")
    str2 = input("List 2: ")
    list1 = str1.split() # string method split() returns a list of strings resulting after cutting the initial string by spaces. 
    list2 = str2.split() 
    set = list(set(list1).intersection(list2)) #  Use set() to convert one of the lists to a set. Find common elements of set and list
    set.sort() # sort method in ascending order
    if str == quit: # exit the loop
        break

    print(set)
