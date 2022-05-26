import os# Complete the solve function below.

def solve(s):
    s = list(s)
    for i in range(len(s)):
        if s[i-1] and s[i-1] == ' ' and s[i].isalpha():
            s[i] = s[i].upper()
    s[0] = s[0].upper()
    return ''.join(s)


if __name__ == '__main__':
    s = input()
    result = solve(s)

    print(result + '\n')
