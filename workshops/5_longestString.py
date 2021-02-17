# Program that prompts for and reads strings until an empty string is entered.
# Print the longest string that was entered.


#declare variable to hold the longest string
longestStr=""
#Run this while loop until user do not enter null string
while True:
#Ask user to enter String input
    sentence = str(input("Enter a string: "))
#Check if entered string is empty
    if(sentence == ""):
        break
#check if longest string length is less than the currently entered string
    if(len(sentence)>len(longestStr)):
        longestStr = sentence
#Print the longest string
print("Longest String is : "+longestStr)
