"""O professor está te ensinando sobre sensores. Este é um elemento muito importante em diversas aplicações. Para aprender melhor os conceitos de precisão o professor pediu para realizar uma montagem prática do sensor Termo Ind v4.0 no novo laboratório de Automação.

Você como bom aluno anotou a fórmula para o cálculo da precisão de um sensor:

σ
=
√
∑
Q
T
1
(
X
i
−
¯¯¯¯¯
X
)
2
Q
T
−
1

Onde QT é a quantidade de vezes que foi realizado o teste,
X
 o valor medido em cada teste e
¯¯¯¯¯
X
 a média dos valores.

Para realizar o teste você ficou H horas fazendo testes, e a cada M minutos você verificou o valor X da temperatura entregue pelo sensor.

Agora que você tem as medidas, e como você tem a habilidade de programar, faça um programa que entregue a precisão do sensor.

Entrada
Existem vários casos de teste, cada caso consiste de duas linhas. A primeira contém dois valores H e M. E a segunda consiste dos valores de ponto flutuante Xi indicando o valor de cada medida do sensor.

É garantido que haverão no mínimo 5 e no máximo 105 medidas por caso e que estes valores estão no intervalo [0, 255] com duas casas decimais.

Saída
Para cada caso de teste, imprima uma única linha com um número indicando a precisão do sensor. O valor calculado deve ser apresentado com 5 dígitos após o ponto decimal."""
from math import sqrt
while True:
    try:
        H, M = (int(x) for x in input().split())
        X = [float(x) for x in input().split()]
        Xm = sum(X)/len(X)
        tot = float()
        qt = (H * 60) / M
        for i in X:
            val = (i - Xm) ** 2
            tot += val
        print(f'{sqrt(tot / (int(qt) - 1)):.5f}')
    except EOFError:
        break

