def findTheDiff(s, t):
    result = None
    a = list(s)
    b = list(t)
    for c in t:
        if c in a:
            b.remove(c)
    return b


if __name__ == '__main__':
    s = input().strip()
    t = input().strip()

    print(*findTheDiff(s, t))
#34 23 1 24 75 33 54 8