#class aluno

class Aluno():

    def __init__(self):
        self.lista_alunos = list()
        self.nome_aluno = ""
        self.apelido_aluno = ""
        self.idade_aluno = ""
        self.morada_aluno = ""
        self.cc_aluno = ""
        self.num_aluno = ""
        pass

    def preencherInfo(self, nome_aluno, apelido_aluno, idade_aluno, morada_aluno, cc_aluno, num_aluno):
        self.nome_aluno = nome_aluno
        self.apelido_aluno = apelido_aluno
        self.idade_aluno = idade_aluno
        self.morada_aluno = morada_aluno
        self.cc_aluno = cc_aluno
        self.num_aluno = num_aluno
        pass

    def mostrarInfo(self, lista): #mostrar info dos alunos existentes

        print("Alunos existentes:\n")

        contador = 0

        if len(lista) > 0:
            for aluno in lista:
                print(contador + 1, " - ", aluno.nome_aluno, aluno.apelido_aluno, "| Nº", aluno.num_aluno)
                print("")
                contador += 1
            pass
        else:
            print(f"Tem {len(lista)} alunos neste momento.\n")

    def InfoCompleta(self):  #mostrar valores completos dos alunos
        print("\nNome: ", self.nome_aluno)
        print("Apelido: ", self.apelido_aluno)
        print("Idade: ", self.idade_aluno)
        print("Morada: ", self.morada_aluno)
        print("Nº de CC: ", self.cc_aluno)
        print("Nº: ", self.num_aluno)
        pass
