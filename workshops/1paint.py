#paint program

# Problem: A painter needs to estimate how much paint is needed for a rectangular wall. Write
# a program that asks the user for the width of the wall in metres, the height of the wall in
# metres, and the volume of paint required in litres per square metre. Print the total litres
# required.

width = float(input("Width of wall (m): "))
height = float(input("Height of wall (m): "))
litresqm = float(input("Litres per square metre: "))

print("Litres required = ", width * height * litresqm)
