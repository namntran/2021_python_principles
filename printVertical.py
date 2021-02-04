# script : printVertical.py
# declare and call a function
#  with an argument, but no return value

def printVertical(x):
    """Print x vertically"""
    for c in str(x):
        print(c)
printVertical("String")
printVertical(42)
