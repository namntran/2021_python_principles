# Problem: A rugby team has 15 players. 
# A bus company has small buses that can carry 10 passengers, 
# and big buses that can carry 38 passengers. 
# Write a program that the tournament organiser can use to calculate 
# how many full teams can be carried in input numbers of small and large buses.

team = 15 #rugby team
big = int(input("How many big buses? ")) #big bus carry 38
small = int(input("How many small buses? ")) #small bus carry 10
passengers = ((big*38)+(small*10))
print ("Number of passengers = ", passengers)
print ("Number of teams = ", passengers//team)