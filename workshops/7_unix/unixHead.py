# file that replicates Unix tool head
# prompts for the name of the file to read, and number of lines to print

path = input("File name: ")
numLines = int(input("Lines: "))
try:
    f = open(path, "r")
    for i in range(numLines):
        line = f.readline()
        print(line, end = "")       
    f.close()
except:
    print("Can't read file '", path, "'.", sep ="")