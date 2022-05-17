"""O seu professor gostaria de fazer um programa com as seguintes características:

Crie 3 variáveis para armazenar uma frase de no máximo 100 caracteres;
Leia uma frase para a primeira variável;
Leia uma frase para a segunda variável;
Leia uma frase para a terceira variável;
Imprima a primeira variável lida no passo 2, a segunda variável lida no passo 3, a terceira variável lida no passo 4.
Não esqueça de pular linha;
Imprima a primeira variável lida no passo 3, a segunda variável lida no passo 4, a terceira variável lida no passo 2.
Não esqueça de pular linha;
Imprima a primeira variável lida no passo 4, a segunda variável lida no passo 2, a terceira variável lida no passo 3.
Não esqueça de pular linha;
Repita o procedimento 5, imprimindo só 10 caracteres de cada variável.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem três linhas. Na primeira linha tem uma
variável A que armazena uma frase de no máximo 40 caracteres. Na segunda linha tem uma variável B que armazena uma
frase de no máximo 40 caracteres. Na terceira linha tem uma variável C que armazena uma frase de no máximo 40
caracteres. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem quatro linhas da forma descrita nos
itens 5, 6, 7 e 8. Conforme mostra o exemplo de saída a seguir."""
a, b, c = (input() for _ in range(3))
print(f'{a}{b}{c}\n{b}{c}{a}\n{c}{a}{b}\n{a[:10]}{b[:10]}{c[:10]}')