hi, mi, hf, mf = map(int, input().split())
h = hf - hi

if h < 0:
    h += 24

m = mf - mi

if m < 0:
    m += 60
    h -= 1

if m == 0 and h == 0:
    h = 24

if h < 0:
    h += 24

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
