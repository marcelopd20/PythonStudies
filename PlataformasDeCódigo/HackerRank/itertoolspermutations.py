from itertools import permutations
a,b = input().split()
for x in sorted(list(permutations(a,int(b)))):
    print(*x,sep='')

