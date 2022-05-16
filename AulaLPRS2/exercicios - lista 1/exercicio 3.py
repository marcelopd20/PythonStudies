from datetime import datetime #importação do modulo datetime
#Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.]
salh = float(input('Informe o seu salário por hora: R$ ')) #entrada pelo usuário do salário
ht = int(input(f'Informe o número inteiro de horas trabalhadas no mês {datetime.today().month}: ')) #entrada das horas trabalhadas
saltot = salh * ht #calcula do salário
print(f'O salário total será de R${saltot:.2f}') #apresentação ao usuário