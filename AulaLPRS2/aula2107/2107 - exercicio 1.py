#Desenvolva um programa que aceite a entrega de dois números
# informados pelo usuário. Informar o resultado da multiplicação dos dois números.
print('-'*40)#imprimi repetindo 40x o que esta nas aspas
print(f'{"a x b":^40}') #título, centralizado no espaço de 40 caracteres
print('-'*40)
a = int(input('Digite o valor de a: '))#permite a entrada de um valor inteiro na var a
b = int(input('Digite o valor de b: '))#permite a entrada de um valor inteiro na var b
m = a * b #var m recebe a multiplicação entre a e b
print(f'O resultado de {a} x {b} é de {m}') #imprimi o resultado para o usuário
