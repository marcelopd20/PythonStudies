a = int(input())
a = set(map(int, input().split()))
b = int(input())
b = set(int(x) for x in input().split())
print(len(b.intersection(a)))