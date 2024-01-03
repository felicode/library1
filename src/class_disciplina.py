#class disciplina

class Disciplina():

    def __init__(self):
        self.lista_professores = list()
        self.listaAlunos = list()
        self.nome_disc = ""


    def preencherInfo(self, nome_disc):
        self.nome_disc = nome_disc
        pass

    def mostrarInfo(self, lista): #mostar info das disciplinas existentes

        print("Disciplinas existentes:\n")
        contador = 0

        if len(lista) > 0:

            for disc in lista:
                print(contador + 1, " - ", disc.nome_disc)
                print("")
                contador += 1
            pass
        else:
            print(f"Neste momento existem {len(lista)} disciplinas.\n")

    def verInscritos(self): #ver inscritos numa disciplina
        print("\nAlunos inscritos:\n")

        for a in self.listaAlunos:
            print(f"Aluno(a) Nº: {a}\n")
        pass

    def verProfInsc(self, disciplina): #ver professores inscritos numa disciplina
        for a in self.lista_professores:
            a.mostrarProfInsc(disciplina)
            print("")
        pass

    def apagar(self, x): #apagar alunos de todas as disciplinas que estiverem inscritos

        for a in self.listaAlunos:
            self.listaAlunos.pop(x)
            break
        pass
