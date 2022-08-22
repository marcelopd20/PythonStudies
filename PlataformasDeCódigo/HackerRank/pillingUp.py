for _ in range(int(input())):
    a = int(input())
    b = [int(x) for x in input().split()]
    if a%2==0:
        for x in range(a//2):
            if b[x] >= b[a-1-x]:
                pass
            else:
                print('No')
        print('Yes')
    else:
        print('No')
