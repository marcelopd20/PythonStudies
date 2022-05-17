
c = dict()
N = int(input())
a = int

for i in range(N):
    word = input()
    if word in c:
        c[f'{word}'] += 1
    else:
        c[f'{word}'] = 1

print(len(c))
for k, v in c.items():
    print(v, end =' ')
