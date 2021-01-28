#number guessing game
#selection with if, elif, else and nested selection

print("You win if you guess the magic number")
n = int(input("Enter a number between 1 - 100: "))
if n == 50:
    print("You win")
elif 11 <= n <= 19:
    print("it's not a teen number")
elif n >= 100:
    print("choose a number less than 100 doofus")
else:
    if n < 50:
        print("Try higher")
    else:
        print("Try lower")
