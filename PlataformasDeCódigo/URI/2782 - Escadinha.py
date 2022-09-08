x = int(input())
N = [int(_) for _ in input().split()]
count = 1
n = 0
for i in range(1, x-1):
    if N[i-1] - N[i] == N[i] - N[i+1]:
        pass
    else:
        count += 1
print(count)