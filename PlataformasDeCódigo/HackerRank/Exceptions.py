# Enter your code here. Read input from STDIN. Print output to STDOUT
for x in range(int(input())):
    try:
        a, b = [x for x in input().split()]
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)