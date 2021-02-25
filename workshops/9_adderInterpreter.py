

# Adder REPL
import string

m = dict()

def get_input():
    s = input('??? ')
    return s

def only_letters(var_name):
    for c in var_name:
        if c not in string.ascii_letters:
            return False
    return True

def only_digits(val):
    for c in val:
        if c not in string.digits:
            return False
    return True

def get_var(var_name):
    if not only_letters(var_name):
        print('Syntax Error.')
        return
    val = input('Enter a value for ' + var_name + ': ')
    if not only_digits(val):
        print('Syntax Error.')
        return
    m[var_name] = int(val)

def print_var(var_name):
    if only_digits(var_name):
        print(var_name)
        return
    if not only_letters(var_name):
        print('Syntax Error.')
        return
    if var_name not in m:
        print(var_name + ' is undefined.')
        return
    print(var_name + ' equals ' + str(m[var_name]))

def copy_var(var, val):
    if not only_letters(var):
        print('Syntax Error.')
        return
    if only_digits(val):
        m[var] = int(val)
        return
    if not only_letters(val):
        print('Syntax Error.')
        return

    if val not in m:
        print(val + ' is undefined.')
        return
    m[var] = m[val]

def add_var(var, val):
    if not only_letters(var):
        print('Syntax Error.')
        return
    if only_digits(val):
        m[var] += val
        return
    if not only_letters(val):
        print('Syntax Error.')
        return

    if val not in m:
        print(val + ' is undefined.')
        return
    m[var] += m[val]

def main():
    # print('Welcome to the Adder REPL.')
    # start the program
    file = input("Script name: ")
    #open the file and read it line by line instead of asking for user input every time
    fp = open(file, 'r') 
    file = fp.readline()

    sons=int(input('Enter a value for sons: '))
    daughters=int(input('Enter a value for daughters: '))
    total=sons+daughters
    print('children equals',total) 

    # while True:
    #     inp = get_input()
    #     if inp == 'quit':
    #         print('Goodbye.')
    #         exit()
    #     parts = inp.split()

        # if len(parts) == 1:
        #     print('Syntax Error.')
        # elif len(parts) == 2:
        #     if parts[0] == 'input':
        #         get_var(parts[1])
        #     elif parts[0] == 'print':
        #         print_var(parts[1])
        #     else:
        #         print('Syntax Error.')
        # elif len(parts) == 3:

        #     if parts[1] == 'gets':
        #         copy_var(parts[0], parts[2])
        #     elif parts[1] == 'adds':
        #         add_var(parts[0], parts[2])
        #     else:
        #         print('Syntax Error')
        # else:
        #     print('Syntax Error')

if __name__ == "__main__":
    main()