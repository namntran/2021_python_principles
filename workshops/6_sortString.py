# Program to sort alphabetically the words form a string provided by the user
quit = ""
sentence = [] # variable to store list of strings
while True:
    str = input("Enter a word: ")
    if str == quit: # exit the loop
        break
    sentence.append(str) # save all the input strings into a list
    sentence.sort() # sort method
# print(sentence) #output string to terminal in one list
print(*sentence, sep='\n') #unpacks the list and sends each element as an argument to print(), with '\n' as a separator.