"""O seu professor gostaria de fazer um programa com as seguintes características:

Crie uma variável inteira;
Crie uma variável real de simples precisão;
Crie uma variável que armazene um carácter;
Crie uma variável que armazene uma frase de no máximo 50 caracteres;
Leia todas as variáveis na ordem da forma criada;
Imprima todas as variáveis como foram lidas;
Imprima as variáveis, separando-as por uma tabulação (8 espaços), na ordem que foram lidas;
Imprima as variáveis com exatos 10 espaços.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem uma linha. A linha tem uma variável A que
armazena um número inteiro, uma variável B que armazena um número real, uma variável C com um carácter e uma variável D
que armazena uma frase de no máximo 50 caracteres. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas da forma descrita nos itens
6, 7 e 8. Conforme mostra o exemplo de saída a seguir. Imprima os valores de ponto flutuante com 6 casas decimais após
a vírgula."""
a = input().split()
t = a[3]
for c in range(4, len(a)):
    t += ' ' + a[c]
a[3] = t
print(f'{a[0]}{a[1]}{a[2]}{a[3]}\n{a[0]} {a[1]} {a[2]} {a[3]}\n{a[0]:>10}{a[1]} {a[2]} {a[3]}')