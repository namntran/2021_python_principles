# digits.py
# Print the number of characters in the string that are decimal digits

n = 0
str = input("Enter a string: ")
for char in str:
    if '0' <= char <= '9':
        n += 1
print("Number of digits: ", n)