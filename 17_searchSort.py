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
            if xs[j] > xs[i]:
               xs[j], xs[i] = xs[i], xs[j]