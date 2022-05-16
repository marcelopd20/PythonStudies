
n = int(input())
num = map(int, input().split())
print(sorted(list(set(num)))[-2])