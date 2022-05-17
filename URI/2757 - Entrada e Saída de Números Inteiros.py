"""O seu professor gostaria que você fizesse um programa com as seguintes características:

Crie três variáveis para armazenar números inteiros;
Leia o primeiro número, que pode ser um valor na faixa de: -10000 ≤ A ≤ 10000;
Leia o segundo número, que pode ser um valor na faixa de: 0 ≤ B ≤ 99;
Leia o terceiro número, que pode ser um valor na faixa de: 0 ≤ C ≤ 999;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável,
 uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número
 armazenado na segunda variável, uma virgula, um espaço em branco, a letra C, um espaço em branco, o sinal de igual, um
 espaço em branco, o número armazenado na terceira variável. Não esqueça de pular linha;
Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a direita;
Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e preenchido com zeros;
Repita o procedimento 5, colocando o número em um espaçamento de 10 dígitos e justificado a esquerda.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem um inteiro
A (-10000 ≤ A ≤ 10000). Na segunda linha tem um inteiro B (0 ≤ B ≤ 99). Na terceira linha tem um inteiro C (0 ≤ C ≤ 999)
. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas da forma descrita no item
5. Conforme mostra o exemplo de saída a seguir."""
def change(num):
    num = str(abs(num))
    return f'-{num:0>9}'


a = '{x:0>10} if x > 0 else change(x)'
x, y, z = (int(input()) for _ in range(3))
print(f"A = {x}, B = {y}, C = {z}")
print(f"A = " f"{x:>10}, B = " f"{y:>10}, C = " f"{z:>10}")
print(f"A = " f"{x:0>10}" if x > 0 else f"A = {change(x)}", end=', ')
print(f"B = " f"{y:0>10}" if y > 0 else f"B = {change(y)}", end=', ')
print(f"C = " f"{z:0>10}" if z > 0 else f"C = {change(z)}")
print(f"A = {x:<10}, B = {y:<10}, C = {z:<10}")