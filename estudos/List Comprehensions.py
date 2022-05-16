from time import sleep

#for usado em uma list of comprehension
lista = [1, 2, 3, 4, 5]
mult5 = [num*5 for num in lista]
print(mult5)

def tabuada(n):
    lst = range(1,11)
    resultado = [num*n for num in lst]
    return (f'Resultados da Tabuada do {n}: {resultado}')

print(tabuada(6))

#List comprehension usando if
print('1 para printar qualquer outro numero da sleep')
a = int(input())
print('List of Comprehension') if a == 1 else sleep(3)
print('\n')
lista1 = [100, 45, 294, 23904, 395, 47895, 233, 2245, 67, 788, 998, 776, 910]
print(lista1)
print('print([x for x in lista1 if x <300])')
print([x for x in lista1 if x <300])#list comprehension  com for e if
print('\n')
print('print([x if x < 300 else "Maior" for x in lista1])')
print([x if x < 300 else "Maior" for x in lista1])

