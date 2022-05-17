"""O seu professor gostaria de fazer um programa com as seguintes características:

Crie duas variáveis para armazenar números reais de precisão simples;
Crie duas variáveis para armazenar números reais de precisão dupla;
Leia o primeiro número de precisão simples que sempre terá uma casa decimal;
Leia o segundo número de precisão simples que sempre terá duas casas decimais;
Leia o primeiro número de precisão dupla que sempre terá três casas decimais;
Leia o segundo número de precisão dupla que sempre terá quatro casas decimais;
Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável
lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em
branco, o número armazenado na segunda variável lida no passo 4. Não esqueça de pular linha;
Imprima a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável
 lida no passo 5, uma virgula, um espaço em branco, a letra D, um espaço em branco, o sinal de igual, um espaço em
 branco, o número armazenado na segunda variável lida no passo 6. Não esqueça de pular linha;
Repita o procedimento 7, imprimindo os números com uma casa decimal;
Repita o procedimento 8, imprimindo os números com uma casa decimal;
Repita o procedimento 7, imprimindo os números com duas casas decimais;
Repita o procedimento 8, imprimindo os números com duas casas decimais;
Repita o procedimento 7, imprimindo os números com três casas decimais;
Repita o procedimento 8, imprimindo os números com três casas decimais;
Repita o procedimento 7, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E;
Repita o procedimento 8, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E;
Repita o procedimento 7, imprimindo somente a parte inteira do número;
Repita o procedimento 8, imprimindo somente a parte inteira do número.
Entrada
A entrada consiste em vários arquivos de teste. Em cada arquivo de teste tem duas linhas. Na primeira linha tem dois
 números reais A e B (-1000.0 ≤ A, B ≤ 1000.0), separados por espaço em branco. Na segunda linha tem dois números reais
 C e D (-1000.0 ≤ C, D ≤ 1000.0), separados por espaço em branco. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem doze linhas da forma descrita no item 7
e 8. Conforme mostra o exemplo de saída a seguir."""
import struct


a, b = map(float, input().split())
c, d = map(float, input().split())
a = struct.unpack('f', struct.pack('f', a))[0]

b = struct.unpack('f', struct.pack('f', b))[0]

print(f'A = {a:.6f}, B = {b:.6f}\nC = {c:.6f}, D = {d:.6f}')
print(f'A = {a:.1f}, B = {b:.1f}\nC = {c:.1f}, D = {d:.1f}')
print(f'A = {a:.2f}, B = {b:.2f}\nC = {c:.2f}, D = {d:.2f}')
print(f'A = {a:.3f}, B = {b:.3f}\nC = {c:.3f}, D = {d:.3f}')
print(f'A = {a:.3E}, B = {b:.3E}\nC = {c:.3E}, D = {d:.3E}')
print(f'A = {a:.0f}, B = {b:.0f}\nC = {c:.0f}, D = {d:.0f}')

