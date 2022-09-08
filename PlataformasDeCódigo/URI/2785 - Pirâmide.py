"""No depósito da fábrica, encostada numa parede, existe uma matriz de N linhas por N colunas de caixas empilhadas. Cada caixa possui um peso inteiro positivo associado. O inspetor da fábrica precisa retirar algumas caixas da matriz de modo a deixar uma espécie de pirâmide de caixas satisfazendo as seguintes restrições:

• Se uma caixa está na pirâmide, a caixa imediatamente abaixo dela também deve estar na pirâmide;

• Na i-ésima linha de caixas (a linha 1 é a do topo da matriz), a pirâmide deve ter exatamente i caixas consecutivas.

Dados os pesos de todas as caixas na matriz, seu programa deve calcular o peso total mínimo que uma pirâmide poderá ter, se o inspetor retirar algumas caixas segundo as restrições acima.

Entrada
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando a dimensão da matriz. As N linhas seguintes contêm, cada uma, N inteiros representando os pesos das caixas em cada linha da matriz de caixas.

Os valores dos elementos da matriz estão entre 1 e 100, inclusive.

Saída
Seu programa deve produzir uma única linha, contendo um inteiro, indicando o peso total mínimo que a pirâmide poderá ter."""

N = int(input())
m = []
p = [[0 for x in range(N)] for _ in range(N)]
print(p)
for n in range(N):
    x = list(map(int, input().split()))
    for i in range(N):
        p[n] += x[i]
    m.append(x)
#for i in range(N):
#    p[i] += m[i]
print(p)

print(m)
