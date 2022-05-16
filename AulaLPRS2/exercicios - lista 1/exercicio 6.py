'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. O programa deverá informar:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''
import datetime #importação da biblioteca datetime
salh = float(input('Informe o seu salário por hora: R$ '))#entrada do salario/hora pelo usuário
ht = int(input(f'Informe o número inteiro de horas trabalhadas no mês {datetime.date.today().month}: ')) #entrad das horas mensais trabalhadas
saltot = salh * ht#calculo do salário total
ir = saltot * 0.11#calculo do imposto de rende
inss = saltot * 0.08#calculo do inss
sind = saltot * 0.05#calculo do sindicato
desc = ir + inss + sind#valor a descontar do salario
saliq = saltot - desc#salário liquido
print(f'''+ Salário Bruto : R$ {saltot:.2f}
- IR (11%) : R$ {ir:.2f}
- INSS (8%) : R$ {inss:.2f}
- Sindicato (5%) : R$ {sind:.2f}
= Salário Liquido : R$ {saliq:.2f}''')#apresentação ao usuario

