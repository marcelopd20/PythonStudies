#Desenvolva um programa que aceite como entrada o valor do raio de um determinado círculo.
# O programa deverá apresentar como resultado a área do círculo em questão.
import math #importação do módulo math
print('-'*30) #imprime 30x o que esta entre aspas
print(f'{"ÁREA DE CIRCULO":^30}') #título do programa centralizado
print('-'*30)
r = int(input('Forneça o valor do raio: ')) #entrada do raio do círculo fornecido pelo usuário
a = math.pow(r, 2) * math.pi #calculo da área utilizando o módulo math, raio ao quadrado vezes pi
print(f'A área do círculo é de {a:.2f} m².') #impressão do resultado para o usuário
