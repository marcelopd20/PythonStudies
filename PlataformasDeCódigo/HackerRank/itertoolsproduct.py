from itertools import product
A,B = [int(x) for x in input().split()],[int(x) for x in input().split()]
for x in product(*(A,B)):
    print(x, end=' ')
