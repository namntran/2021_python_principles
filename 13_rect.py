# rect.py
# Print a rectange (rows and columns) of hashes

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
for j in range(rows):
    for i in range(cols):
        print("#", end = "")
    print()