# concertTheatre.py
# write a program so that max 100 seats are sold

def getTickets():
    while(True): # runs until break is reached
        try: # try to get integer
            num = int(input("How many in your group? "))
            break # leave loop
        except (ValueError, NameError):
            print("Only enter an integer.")
    return num

# main function

seats = 100 # number of seats available currently
    
while(True): # runs until break is reached
    print("Seats remaining: ", seats)    
    # check if all seats are sold out
    if seats == 0:
        print("SOLD OUT")
        break;
        
    # try to book seats
    num = getTickets() # get group size
        
    # compare group size to available seats
    if num > seats: # not enough seats left
        print("Sorry, not enough seats left.")
        
    elif num <= seats: # enough seats left
        seats -= num # book seats minus number of tickets sold (group numbers)
        print("Booked, thank you.")
               




