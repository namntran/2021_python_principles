# returns the length of the longest sequence of numbers that form an arithmetic progression
    
def get_max_seq():
    input_text = input("List: ")
    str_list = input_text.split()#split using whitespaces
    num_list = list(map(int,str_list))#map each string in the list to a number
    
    if(len(num_list)==1): return 1
    #create list of all 2s since that is the minimum arithmetic  sequence size, maximum number of sequences is length of the list
    seq_sizes = []
    for i in range(len(num_list)):
        seq_sizes.append(2)
    
    seq_loc = 0
    current_diff = num_list[1]-num_list[0]#get the first diff
    for i in range(1,len(num_list)-1):
        diff = num_list[i+1]-num_list[i]#get next diff
        if(diff==current_diff):#if differences are the same, there is another item that can be added to the current sequence
            seq_sizes[seq_loc]+=1
        else:
            current_diff = diff#new difference to check
            seq_loc +=1#new location to add the sequence size
    
    print (max(seq_sizes))#return the max sequence stored in seq_sizes

while True: # sentinel pattern
    get_max_seq()

    
