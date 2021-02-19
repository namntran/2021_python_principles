# Program that prints the number of lines of hashes
# doubles the number of hashes on each line

num = int(input("How many lines: "))
list2 = []

for i in range(0,num):
    list2 = (2**i)
    print("#" * list2)


