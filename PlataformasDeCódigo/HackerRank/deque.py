from collections import deque

dq = deque()
for _ in range(int(input())):
    a = input().split()
    if len(a) == 2:
        eval(f'dq.{a[0]}({a[1]})')
    else:
        eval(f'dq.{a[0]}()')
print(*dq)