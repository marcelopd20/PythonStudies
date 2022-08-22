n = int(input())
s = set(map(int, input().split()))
for x in range(int(input())):
    y = input().split()
    if len(y) == 2:
        eval(f's.{y[0]}({y[1]})')
    else:
        eval(f's.{y[0]}()')
print(sum(s))