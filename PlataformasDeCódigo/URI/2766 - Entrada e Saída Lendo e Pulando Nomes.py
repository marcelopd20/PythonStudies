"""O seu professor gostaria de fazer um programa com as seguintes características:

Leia 10 nomes, sem espaço em branco;
Imprima o terceiro nome da lista;
Imprima o sétimo nome da lista;
Imprima o nono nome da lista.
Entrada
A entrada consiste vários arquivos de teste. Em cada arquivo de teste tem dez linhas. Em cada linha tem um nome de no
máximo 30 caracteres e sem espaço em branco. Conforme mostrado no exemplo de entrada a seguir.

Saída
Para cada arquivo da entrada, terá um arquivo de saída. O arquivo de saída tem três linhas conforme os procedimentos 2,
3 e 4. Conforme mostra o exemplo de saída a seguir."""
a = [input() for _ in range(10)]
print(f'{a[2]}\n{a[6]}\n{a[8]}')