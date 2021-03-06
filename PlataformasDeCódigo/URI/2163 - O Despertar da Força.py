"""Há muito tempo atrás, em uma galáxia muito, muito distante...

Após o declínio do Império, sucateiros estão espalhados por todo o universo procurando por um sabre de luz perdido.
Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um
sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo para um terreno 4 x 7 com um sabre de
luz nele (na posição (2, 4)).

Você deve escrever um programa que, dado um terreno N x M, procura pelo padrão do sabre de luz nele. Nenhuma
varredura tem mais do que um padrão de sabre de luz.

Entrada
A primeira linha da entrada tem dois números positivos N e M, representando, respectivamente, o número de linhas e
de colunas varridos no terreno (3 ≤ N, M ≤ 1000). Cada uma das próximas N linhas tem M inteiros, que descrevem os
valores lidos em cada célula do terreno (-100 ≤ Tij ≤ 100, para 1 ≤ i ≤ N e 1 ≤ j ≤ M).

Saída
A saída é uma única linha com 2 inteiros X e Y separados por um espaço. Eles representam a coordenada (X,Y) do sabre
de luz, caso encontrado. Se o terreno não tem um padrão de sabre de luz, X e Y são ambos zero."""
n = input().split()
N, M = int(n[0]), int(n[1])
mat = list()
x = y = 0
resp = False
for l in range(N):
    mat.append([int(x) for x in input().split()])
for l in range(1, N-1):
    if resp:
        break
    for c in range(1, M-1):
        if mat[l][c] == 42:
            if mat[l-1][c-1] == mat[l-1][c] == mat[l-1][c+1] == 7:
                if mat[l][c-1] == mat[l][c+1] == 7:
                    if mat[l+1][c-1] == mat[l+1][c] == mat[l+1][c+1] == 7:
                        x = l+1
                        y = c+1
                        resp = True
                        break
print(f'{x} {y}')
