#Tendo como dados de entrada a altura de uma pessoa,
# construa um programa que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Informe a sua altura: ')) #entrada da altura pelo usuário
peide = (72.7*altura) - 58 #calculo do peso ideal
print(f'O peso considerado ideal para o seu tamanho é {peide:.2f} Kg.') #apresentação do resultado ao usuário
print(f'Obs: esse valor é apenas uma referencia, podendo variar conforme caracteristicas individuais.') #mensagem ao usuário
