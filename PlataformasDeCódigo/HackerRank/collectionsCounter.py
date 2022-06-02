from collections import Counter

x = int(input())
stk = Counter([int(x) for x in input().split()])
ed = 0
for t in range(int(input())):
    k, p = (int(x) for x in input().split())
    if k in stk.keys() and stk[k] > 0:
        ed += p
        stk[k] -= 1
print(ed)
