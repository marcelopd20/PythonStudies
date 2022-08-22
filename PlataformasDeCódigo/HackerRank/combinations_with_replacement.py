from itertools import combinations_with_replacement

a, n = input().rsplit(sep=' ', maxsplit=-1)
a = [x for x in a]
a.sort()
a = combinations_with_replacement(a, int(n))
for x in a:
    print(*x, sep='')