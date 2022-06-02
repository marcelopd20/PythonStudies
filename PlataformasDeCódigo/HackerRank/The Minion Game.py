def minion_game(string):
    vws = 'AEIOU'
    s1 = len(string)
    n = int(s1*(s1+1)/2)
    k = sum(s1 - i for i in range(s1) if string[i] in vws)
    s = n - k
    print(f'Kevin {k}' if k > s else 'Draw' if k == s else f'Stuart {s}')

if __name__ == '__main__':
    s = input()
    minion_game(s)