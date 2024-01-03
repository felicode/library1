#funcoes

def menu(): #opcoes do menu
    print("1 - Criar Disciplina")
    print("2 - Listar Disciplinas")
    print("3 - Eliminar Disciplina")
    print("4 - Criar Aluno")
    print("5 - Inscrever Aluno")
    print("6 - Listar Alunos")
    print("7 - Eliminar Aluno")
    print("8 - Listar Alunos inscritos numa dada disciplina")
    print("9 - Criar Professor")
    print("10 - Adicionar professor a uma disciplina")
    print("11 - Lista de professores para cada disciplina")
    print("12 - Importar alunos de um ficheiro")

    print("\n0 - Sair")
    pass


def menu_importar(): #opcoes do menu de importacao
    print("\n11 - Importar alunos de um ficheiro")
    print("\n1 - Importar ficheiro (disciplinas, alunos e professores)\n")
    print("2 - Importar alunos para uma disciplina\n")


def voltar(): #Enter para retornar

    while True:
        enter = input("Pressione Enter para retornar..")
        print("")
        if not enter:
            break


def input_str(texto): #receber input do utilizador e validar, numeros e caracteres especiais
    while True:
        user = input(texto)
        if any(i.isdigit() for i in user) or any(not i.isalnum() for i in user):
            print("\nEste campo deve conter somente letras.\n")
        elif ' ' in user or len(user) == 0:
            print("\nEste campo não deve conter espaços.\n")
        else:
            break
    return user
    pass


def input_idade(texto): #receber inpput do utilizador, validar idade entre 18 a 100 e erro do int
    while True:
        idade_user = input(texto)
        try:
            idade = int(idade_user)
            if idade >= 18 and idade <= 100:
                break
            else:
                print("\nIdade deve estar entre 18 e 100.\n")
        except:
            print("\nEste campo deve conter apenas números inteiros.\n")
    return idade
    pass


def input_num(texto): #receber input do utilizador, validar erro do int
    while True:
        num_user = input(texto)
        try:
            num = int(num_user)
            break
        except:
            print("\nEste campo deve conter apenas números inteiros.\n")
    return num
    pass
