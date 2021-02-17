#program to calculate cheapest cost of bus

teams = int(input("How many teams? "))
n=teams*15  #rugby team of 15 players
big=0
small=0
cost=0.0
print("passengers: ", n)

while(n>=0): #sentinel value = 0 (-n)
    if(n>20):# calculate number of big buses required (small bus fit 10 passengers)
        cost=cost+200
        n -= 48 # loop counter (big bus fit 48 passengers)
        # print("passengers: ", n)      
        big += 1  #number of big buses required
        
    elif(n<=20): # calculate number of small buses required (fit 10 passengers)
        cost=cost+95
        n -= 10 # loop counter (small bus fit 10 passegers)
        small+=1
       
print("Hire", big, "big buses and", small, "small buses. Cost =  $", cost)