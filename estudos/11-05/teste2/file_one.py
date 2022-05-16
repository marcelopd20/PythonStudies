import file_two

print(f'__name__ no arquivo um está definido como: {__name__}\n')

if __name__ == '__main__':
    print("Arquivo um executado diretamente.\n")
else:
    print("Arquivo um executado ao ser importado\n")