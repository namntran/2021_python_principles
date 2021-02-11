# file: whatModules.py
# prompt for the name of a python file and 
# print the names off all the modules it imports

path = input("Enter a script name: ")
try:
    f = open(path)
    modules = []
    for line in f:
        # print(line, end = "") #temp
        words = line.split()
        # print(words) #temp
        if len(words) >= 2 and (words[0] == 'import' or words[0] == 'from'):
            modules.append(words[1])
            # print("MODULE", words[1], modules)
    f.close()
    print("Modules imported:", end = "")
    for m in modules[:-1]: #take slice except for last element to get ,
        print(" ", m, ",", sep = "", end = "")
    if modules != []:
            print(" ", modules[-1], sep = "", end = '.\n')
    else:
        print(" <none>")
except:
    print("Can't read file '", path, "'.", sep ="")


