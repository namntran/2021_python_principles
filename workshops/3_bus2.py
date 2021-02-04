# Problem: A rugby team has 15 players. A bus company has only big buses that can carry 38 passengers.
# Write a program that the tournament organiser can use to calculate the number  of big buses that should be hired.

t = float(15)
b = float(38)
 



n = int(input("How many teams? "))
numPlayers = t * n
print("Number of players = ", numPlayers)

numBus = t * n / b
print(t,n,b)
print(numBus)
if numBus > 1:
    print("Number of big buses = ", numBus)
else:
    print("Number of big buses = ", numBus + 1)