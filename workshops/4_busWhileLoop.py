#program to calculate passenger and cost to hire bus

import math

num_teams = int(input('Enter number of teams: '))
passengers = num_teams*15
num_small = int(math.ceil(passengers/10)) #number of small buses
# math.ceil(x) returns the smallest integer not less than x.
num_large = 0
min_num_small = num_small # to keep track of number of small buses which gives minimum cost
min_num_large = num_large #to keep track of number of large buses which gives minimum cost
min_cost = num_small*95 #initial cost assuming all small buses

while passengers>0:
  num_large += 1
  passengers -= 48 #decrease number of passengers by 48 per large bus
  if passengers>0: 
    #if there are passengers then we need small __build_class
    num_small = int(math.ceil(passengers/10))
  else:
    num_small = 0
  cost = num_large*200 + num_small*95
  if cost<min_cost:
    min_cost = cost
    min_num_large = num_large
    min_num_small = num_small

print('Book',min_num_small,'small buses and',min_num_large,'large buses')
print('The minimum cost is = $', min_cost)
