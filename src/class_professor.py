#class professor


class Professor():

    def __init__(self):
        self.lista_prof = list()
        self.nome_prof = ""
        self.apelido_prof = ""
        self.idade_prof = ""
        self.morada_prof = ""
        self.catprofi_prof = ""
        self.anosexp_prof = ""
        self.num_prof = ""
        pass

    def preencherInfo(self, nome_prof, apelido_prof, idade_prof, morada_prof, catprofi_prof, anosexp_prof, num_prof):
        self.nome_prof = nome_prof
        self.apelido_prof = apelido_prof
        self.idade_prof = idade_prof
        self.morada_prof = morada_prof
        self.catprofi_prof = catprofi_prof
        self.anosexp_prof = anosexp_prof
        self.num_prof = num_prof
        pass

    def mostrarInfo(self, lista): #mostar info dos professores

        print("\nProfessores existentes:\n")
        contador = 0

        for prof in lista:
            print(contador + 1, " - ", prof.nome_prof, prof.apelido_prof, " | Nº", prof.num_prof)
            print("")
            contador += 1
        pass

    def InfoCompleta(self):  #mostrar info completa dos professores
        print("\nNome: ", self.nome_prof)
        print("Apelido: ", self.apelido_prof)
        print("Idade: ", self.idade_prof)
        print("Morada: ", self.morada_prof)
        print("Categoria profissional: ", self.catprofi_prof)
        print("Anos de experiência: ", self.anosexp_prof)
        print("Nº de professor: ", self.num_prof)
        pass

    def mostrarProfInsc(self, disciplina): #mostar valores de professores inscritos numa disciplina
        print(f"Disciplina {disciplina}: ""Professor(a):", self.nome_prof, self.apelido_prof, "| Nº", self.num_prof)
        pass
