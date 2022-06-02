x = int(input())
N = [int(_) for _ in input().split()]
count = 1
n = 0
while N[n] - N[n-1] == N[n-1] - N[n-2]:
    if n == len(N)-1:
        break
    else:
        n += 1
else:
    count += 1
print(count)