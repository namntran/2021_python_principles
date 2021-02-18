# program to test if string contains no digits

while True: # sentinel pattern
    contains_digit = True
    str = input(("Enter a string: "))
    for char in str: # Iterate over `str`
        if char.isdigit(): # Test for digit
            contains_digit = False
    print("Has no digits: ", contains_digit)
