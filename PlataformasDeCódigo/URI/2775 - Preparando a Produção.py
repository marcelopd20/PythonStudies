"""Uma montadora de carros, permite que os usuários criem seus próprios projetos de veículos da maneira que desejar e ainda compartilhar tais informações com outros usuários com o intuito de criar uma rede de utilizadores bem diversificada. O processo se inicia com o cliente desenvolvendo seu próprio modelo através de um software, logo após a conclusão, os dados do projeto são armazenados e de acordo com a disponibilidade da montadora vão sendo realizados.

Porém uma falha na entrega das peças para a montadora está atrasando os pedidos. Acontece que as peças são entregues em pacotes, etiquetados com um número, que deveriam estar ordenados de forma crescente para que a produção inicie. A falha é que os pacotes estão sendo entregues de uma forma aleatória. Você deve criar um programa em que dados a ordem de entrega dos pacotes e o tempo que cada um deles leva para ser trocado de posição, calcule o tempo total para organizar os pacotes. Sabe-se que para efeito de organização dentro da empresa, os pacotes devem ser trocados de posição somente dois a dois e se estiverem um do lado do outro.

Entrada
A entrada consiste de vários casos de testes, lidos até EOF. Para cada caso, o primeiro valor da entrada é um inteiro N (1 <= N <= 1000) representando a quantidade de pacotes, logo após haverá duas linhas com N inteiros cada, com os números dos pacotes, na ordem da entrega, e o tempo, em segundos, que o n-ésimo pacote leva para ser trocado de lugar, respectivamente.

É garantido que os números dos pacotes para cada caso de teste forma uma permutação dos inteiros de 1 a N, e que nenhum pacote demora mais do que um minuto para mover.

Saída
Seu programa deve apresentar, para cada caso de teste, um único inteiro que representa o tempo total para organizar os pacotes."""


"""while True:
    try:
        n = int(input())
        ord = list(map(int, input().split()))[:n]
        wrk = list(map(int, input().split()))[:n]
        time = 0
        while len(ord) > 2:
            while ord and ord[0] == min(ord):
                ord.pop(0)
                wrk.pop(0)
            if ord:
                idx = ord.index(min(ord))
                time += wrk[idx] + wrk[idx - 1]
                ord[idx], ord[idx - 1], wrk[idx], wrk[idx - 1] = ord[idx - 1], ord[idx], wrk[idx - 1], wrk[idx]
        print(time)

    except EOFError:
        break"""


while True:
    try:
        n = int(input())
        ord = list(map(int, input().split()))
        wrk = list(map(int, input().split()))
        time = 0
        while len(ord) > 1:
            idx = ord.index(min(ord))
            time += sum(wrk[:idx]) + (idx * wrk[idx])
            wrk.pop(idx)
            ord.pop(idx)
        print(time)
    except EOFError:
        break