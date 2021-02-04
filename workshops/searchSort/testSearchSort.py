import searchSort
ys = [2, 1, 3, 0, 4, 5]
print(ys)
searchSort.sort(ys)
print(ys) 

ys = []
print(ys)
searchSort.sort(ys)
print(ys)

ys = [3]
print(ys)
searchSort.sort(ys)
print(ys)

ys = [2, 1, 3, 2]
print(ys)
searchSort.sort(ys)
print(ys)

zs = []
print(searchSort.search(3, zs))

zs = [1, 2, 4, -27]
print(searchSort.search(3, zs))

zs = [1, 2, 4, -27]
print(searchSort.search(4, zs))

zs = []
print(searchSort.search2(3, zs))

zs = [1, 2, 4, -27]
print(searchSort.search2(3, zs))

zs = [1, 2, 4, -27]
print(searchSort.search2(4, zs))