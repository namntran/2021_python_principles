# searchSort.py
# write a function that sorts a list in place
# without sorting functions

# write a function that searches a list for the
# first occurrence of a given value 
# without using searching functions

"""Functions for searching and sorting."""

def sort(xs):
    """Sort list xs in place into non-descending order"""
    for i in range(0, len(xs) - 1):
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[i]:
               xs[j], xs[i] = xs[i], xs[j]

def search(x, xs):
    """Returns the index of the first occurence of x in xs, or None if not found."""
    for i in range(0, len(xs)):
        if xs[i] == x:
            return i
    return None

def search2(x, xs):
    """Returns the index of the first occurence of x in xs, or None if not found."""
    i = 0
    j = len(xs)
    while i < j:
       if xs[i] == x:
            j = i
       else:
            i += 1
    if i < len(xs):
        return 
    else:
        return None
        
