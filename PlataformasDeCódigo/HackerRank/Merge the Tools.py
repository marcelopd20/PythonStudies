def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = ''
        for a in string[i:i+k]:
            s += a if a not in s else ''
        print(s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)