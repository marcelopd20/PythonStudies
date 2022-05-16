from sys import stdin, stdout

values = {str(x): [x*(10**y) for y in range(6)] for x in range(10)}
arr = [0 for x in range(1000000)]
prefix = [0 for x in range(1000000)]

for line in stdin:

    n = int(line);

    for i in range(n):

        ch = stdin.read(1)
        while(not ch.isdigit()):
            ch = stdin.read(1)

        par = ch
        ch = stdin.read(1)
        while(ch.isdigit()):
            par += ch
            ch = stdin.read(1)

        arr[i] = 0

        pot = 0
        for digit in par[::-1]:
            arr[i] += values[digit][pot]
            pot += 1

    while(ch != '\n'):
        ch = stdin.read(1)

#------------ SOLVE ---------------#

    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    ans = arr[0]

    for i in range(0, n-1):
        ans = min(ans, abs(prefix[i] - (prefix[n-1] - prefix[i])))

    stdout.write(str(ans) + '\n')