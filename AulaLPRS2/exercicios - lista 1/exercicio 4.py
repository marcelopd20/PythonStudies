#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
F = float(input(f'Temperatura em Fahrnheit: ')) #entrada da temperatura em ºf
C = 5 * ((F-32)) / 9 #conversão da temperatura
print(f'A temperatura em Celsius é de {C:.1f}°C.') #apresentação do resultado para o usuário
