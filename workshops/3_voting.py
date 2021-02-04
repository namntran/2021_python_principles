# Problem: There are three candidates standing for Lord Mayor of Wobatville, Angus, Betty,
# and Cathy. If in the first round of voting, no candidate has more than 50 % of the votes
# another round of voting will be required. Write a program that inputs the numbers of votes
# for each candidate in the first election and declares its result, either:
# • the name of the outright winner, or
# • the names of the two or three candidates to be voted on in the next round of voting.

a = int(input("How many votes for Angus? "))
b = int(input("How many votes for Betty? "))
c = int(input("How many votes for Cathy? "))

# a = "Angus"
# b = "Betty"
# c = "Cathy"

total = a + b + c
percentage = total/2

print (total)
print (percentage)

if (percentage > b + c):
    print("Angus wins.")
elif (percentage > a + c):
    print("Betty wins.")
elif (percentage > a + b):
    print("Cathy wins")
else:
    print("Next round: ", a, b, c)
