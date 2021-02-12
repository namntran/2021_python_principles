# Problem: A rugby team has 15 players. A bus company has only big buses that can carry 38 passengers.
# Write a program that the tournament organiser can use to calculate the number of big buses that should be hired.

# 1. ask number of teams
# 2. calculate the number of teams and remainder (user input * 15)
# 3. find out and  output the number of big buses

t = float(15)
b = float(38) 
n = int(input("How many teams? "))
numPlayers = t * n
remainder = numPlayers % 38

print("Number of players: ", numPlayers)
# print("remainder:", remainder)
if remainder > 0:
    print ("Number of buses to hire: ", int(numPlayers//b+1))
else:
    print("Number of buses to hire: ", int(numPlayers//b))
