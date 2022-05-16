from file_two import function_three

print(f'__name__ no arquivo um está definido como: {__name__}\n')

def function_one():
    print("Função um é executada\n")

def function_two():
    print("Função dois é executada\n")



if __name__ == '__main__':
    print("Arquivo um executado diretamente.\n")
    function_two()
    #file_two.function_three()
    function_three()
else:
    print("Arquivo um executado ao ser importado\n")