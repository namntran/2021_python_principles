# wordsCount.py
# reads file and prints the unique words and how oftern they occurred in decreasing order of frequency.

def cleanUpWord(s):
    s = s.upper()
    s = s.strip("`\"'.,!?-:;()[]{}")
    return s

freqs = dict() # mapping words -> frequencies
path = input("Enter a filename: ")
f = open(path)
for line in f:
    words = line.split()
    for word in words:
        cword = cleanUpWord(word)
        freqs[cword] = freqs.get(cword, 0) + 1
f.close()
wfs = freqs.items()
fws = [(fr, w) for (w, fr) in wfs] #use list comprehension instead of initialise list and append list
# fws = [] #initialise list
# for (w,fr) in wfs:
#     fws.append((fr, w))
fws.sort(reverse = True)
for (fr, w) in fws: 
    print("{:6d}   {:<}".format(fr, w))