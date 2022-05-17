
print(f"__name___ no arquivo dois está definido como: {__name__}\n")

def function_three():
    print("Função três é executada\n")

def function_four():
    print("Função quatro é executada\n")


if __name__ == '__main__':
    print('Arquivo dois exetado diretamente\n')
else:
    print('Aqruivo dois executado ao ser importado\n')
