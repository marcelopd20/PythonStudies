from string import ascii_lowercase
def print_rangoli(size):
    alpha = ascii_lowercase
    prt = []
    for i in range(size):
        s = '-'.join(alpha[i:size])
        prt.append((s[::-1]+s[1:]).center(4*size-3, '-'))
    print('\n'.join(prt[:0:-1]+prt))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)