"""O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Crie duas variáveis reais de dupla precisão;
Atribua a primeira o valor 234.345 e a segunda o valor 45.698;
Imprima as duas variáveis com seis casas decimais;
Imprima as duas variáveis sem nenhuma casa decimal;
Imprima as duas variáveis com uma casa decimal;
Imprima as duas variáveis com duas casas decimais;
Imprima as duas variáveis com três casas decimais;
Imprima as duas variáveis com notação cientifica com 'e';
Imprima as duas variáveis com notação cientifica com 'E';
Imprima as duas variáveis com a representação mais curta, com 'e' ou 'E' ou sem;
Imprima as duas variáveis com a representação mais curta, com 'e' ou 'E' ou sem;
Para imprimir, separe os valores com um espaço em branco, um traço (-) e um espaço em branco."""
a = 234.345
b = 45.698
print(f'{a:.6f} - {b:.6f}\n'
      f'{int(round(a))} - {int(round(b))}\n'
      f'{a:.1f} - {b:.1f}\n'
      f'{a:.2f} - {b:.2f}\n'
      f'{a:.3f} - {b:.3f}\n'
      f'{a:e} - {b:e}\n'
      f'{a:E} - {b:E}\n'
      f'{a} - {b}\n'
      f'{a} - {b}')
