# import math

n = int(input('Enter number of teams: '))
passengers = n*15
# num_small = int(math.ceil(passengers/10)) #number of small buses
# math.ceil(x) returns the smallest integer not less than x.
small = 0
big = 0
cost = 0.0
min_num_small = small # to keep track of number of small buses which gives minimum cost
min_num_large = big #to keep track of number of large buses which gives minimum cost
min_cost = small*95 #initial cost assuming all small buses

while(n>=0):
    if(n>20):# small bus capacity of 10 passengers
        cost  = cost+200
        n = n-48 # big bus capacity of 48 passengers
        big = big+1
    elif(n<=20):
        cost=cost+95
        n=n-10
        small+=1
    if cost<min_cost:
        min_cost = cost
        min_num_large = big
        min_num_small = small

print('Book',min_num_small,'small buses and',min_num_large,'large buses')
print('The minimum cost is = $', min_cost)

# while(n>=0):
#     if(n>20):# small bus capacity of 10 passengers
#         cost  = cost+200
#         n = n-48 # big bus capacity of 48 passengers
#         big = big+1
#     elif(n<=20):
#         cost=cost+95
#         n=n-10
#         small+=1
# print("Hire", big, "big buses and", small, "small buses. Cost =  $", cost)