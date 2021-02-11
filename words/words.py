# words.py
# reads file and prints the unique words in ascending order.
def cleanUpWord(s):
    s = s.upper()
    s = s.strip("`\"'.,!?-:;()[]{}")
    return s

uniqueWords = set()
path = input("Enter a filename: ")
f = open(path)
for line in f:
    words = line.split()
    # print(words)
    for word in words:
        uniqueWords.add(cleanUpWord(word))
f.close()
for word in sorted(uniqueWords):
    print(word)