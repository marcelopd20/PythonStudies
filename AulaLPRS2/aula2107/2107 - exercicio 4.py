import os
#O dono de uma padaria deseja um programa para informar o valor com desconto para
# pagamentos a vista em uma. O pagamento a vista possuí um desconto de 5% em cima
# do valor total . O programa deverá aceitar como entrada o valor total da compra
# e informar o valor a vista da mesma.
print('-*'*21)#imprime 21x o que esta entre aspas
print(f'{"PADARIA PÃO VÉIO":^42}') #Título centralizado no espaço de 42 caracteres
print('-*'*21)
print('O pagamento a vista possui desconto de 5%.')#Informe o que o processamento realiza
vlr= float(input('Valor a vista R$ '))#entrada do usuário do valor
print(f'O valor a vista é de \033[30mR$ {vlr*0.95:.2f}\033[m.')#imprimi o valor com descontro para o usuário
