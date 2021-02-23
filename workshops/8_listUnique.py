# program that returns the list of all the elments in the first list 
# that do no occur in the second list
def find_unique(list1,list2):
    '''function to find the list of all the elements in the 
    first list that do not occur in the second list.'''

    result=[] #empty list to store the result
    for i in list1: #iterate over first list
        if i not in list2: #if item not in second list
            result.append(i) #then append element to result

    return result #return list

quit = ""

while True: # sentinel pattern
    list1 = input("List 1: ")
    list2 = input("List 2: ")

    if str == quit:  # exit the loop
        break

    # print(*find_unique(list1, list2))
    print(find_unique(list1, list2))
    
