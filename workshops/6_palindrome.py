# palindrome program to check if reverse and original of string are same or not.
quit = ""

while True: # run this loop until user enters blank
    sentence = input("Enter a string: ") # ask user to enter string input
    string1 = sentence.upper() # convert string to upper case to compare
    mirror = string1[::-1] # function which returns reverse of a string
    print("Reverse string in upper case: ", mirror)

    if(sentence == quit): # check if entered string is empty
        break
    if string1 == mirror: # compare strings
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")
