"""Com o advento dos conceitos da Indústria 4.0 e a evolução da internet das coisas, se tornou simples acompanhar todas as etapas da produção de um produto em uma linha de montagem. De posse das informações, é possível otimizar a produção e diminuir o tempo gasto até que esteja pronta.

Uma indústria apresenta o seguinte esquema de produção:



Sabendo o tempo gasto em cada estação, e o tempo para trocar entre as duas linhas de montagem, calcule o menor tempo em que é possível realizar a produção de um item.

Entrada
A entrada possui vários casos de teste (EOF). A primeira linha contém um inteiro N, o número de etapas na linha de produção. A segunda linha contém dois inteiros e1 e e2, o tempo gasto para a entrada em cada uma das linhas de produção. A próxima linha possui N valores, a11, a12, ..., a1n, representando o tempo gasto para executar a iésima etapa na linha 1. A próxima também conterá  N valores, a21, a22, ..., a2n com os tempos de cada etapa na linha 2. As próximas duas conterá N-1 inteiros representando os tempos de transição da linha 1 para a linha 2,  t11, t12, ..., t1n-1 e da linha 2 para a linha 1,  t21, t22, ..., t2n-1, respectivamente. Por fim, mais dois inteiros x1 e x2 representando o tempo de saída de cada linha.

Considere que número de etapas por caso de teste estará entre 1 e 1000 e os demais valores entre 0 e 105.

Saída
A saída deve mostrar o tempo mínimo gasto na produção."""
while True:
    try:
        n = int(input())
        e1, e2 = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        a1[0] += e1
        a2[0] += e2
        t = a1[0] if a1[0] < a2[0] else a2[0]
        idx = True if a1[0] < a2[0] else False
        t1 = list(map(int, input().split()))
        t2 = list(map(int, input().split()))
        x1, x2 = list(map(int, input().split()))
        a1[n-1] += x1
        a2[len(a2)-1] += x2
        t3 = 0
        for x in range(0,n-1):
            print(f'idx: {idx}, t3: {t3}, x+1: {x+1}, t: {t},\na1[x+1]: {a1[x+1]}, a2[x + 1] + t1[x]: {a2[x + 1] + t1[x]},\na2[x + 1]: {a2[x + 1]}, a1[x + 1] + t2[x]: {a1[x + 1] + t2[x]}\n\n')
            if idx:
                if a1[x + 1] <= a2[x + 1] + t1[x]:
                    t += a1[x+1]
                else:
                    t += a2[x+1]+t1[x]
                    idx = False
            else:
                if a2[x + 1] <= a1[x + 1] + t2[x]:
                    t += a2[x+1]
                else:
                    t += a1[x + 1] + t2[x]
                    idx = True
            #print(t-t3)
            t3 = t
        #print(t)


    except EOFError:
        break
