from itertools import combinations

s,n = input().rsplit(sep=" ", maxsplit=-1)
s = [x.upper() for x in s]
s.sort()
for y in range(1,int(n)+1):
    t = combinations(s, int(y))
    for x in t:
        print(*x,sep='')