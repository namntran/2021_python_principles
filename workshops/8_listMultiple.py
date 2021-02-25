# function returns list of all elements that occur multiple times in both lists

def multiple_elements(list1,list2):
    result=[]
    for i in list1: #for each item in list1
        if list1.count(i)>1 and list2.count(i)>1 and i not in result:#each item that occurs more than once
            result.append(i) #add item to result
    return list(set(result))

quit = ""

while True: # sentinel pattern
    list_elements=input('Lists: ')
    # print(list_elements) #temp

    list_elements=list_elements.split(';') # use string split method() to specify semicolon to split list (normally whitespace)
    # returned value from map() can be passed to functions like list() (to create a list), set() (to create a set)
    list1=list(map(int,list_elements[0].split())) # list1 [0] is list before semicolon
    list2=list(map(int,list_elements[1].split())) # list2 [1] is list after semicolon

    if str == quit:  # exit the loop
        break
    # print("List1: ", list1) #temp
    # print("List2: ", list2) #temp
    print(multiple_elements(list1,list2))
  

