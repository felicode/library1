#main

#importacoes
from class_disciplina import Disciplina
from class_aluno import Aluno
from class_professor import Professor
from funcoes import menu, menu_importar, voltar, input_str, input_idade, input_num
from bd import c, db
#import pandas as pd

#Inicio do programa

lista_discs = list()
lista_alunos = list()
lista_profs = list()

disc = Disciplina() #disc = disciplina objecto
aluno = Aluno()  # objeto Aluno
prof = Professor()  # prof = professor objecto

escolha = 1000

while escolha != 0:

    menu()

    try:
        escolha = int(input("\nEscolha a opção: "))

        if escolha == 1:  # Criar Disciplina

            print("\n1 - Criar Disciplina\n")

            while True: #input e validar se existe disciplinas com o mesmo nome
                user = "Insira o nome da disciplina: "
                nome_disc = input_str(user)
                for i in lista_discs:
                    if nome_disc == i.nome_disc:
                        print(f"\nDisciplina - {nome_disc} já existe.\n")
                        break
                    else:
                        continue
                else:
                    break
                pass

            disc = Disciplina()
            disc.preencherInfo(nome_disc) #preencher disciplina
            lista_discs.append(disc)

            query = f"insert into disciplinas (nome) values ('{nome_disc}')" #query para inserir disciplina
            c.execute(query)
            db.commit()

            print(f"\nDisciplina - {nome_disc} criada.\n")
            voltar()

        elif escolha == 2:  # Listar Disiciplinas

            print("\n2 - Listar Disciplinas\n")

            flag = 0

            if flag < len(lista_discs): #verificar se existem disciplinas
                disc.mostrarInfo(lista_discs) #mostar lista de disciplinas
                voltar()
            else:
                print(f"Existem {len(lista_discs)} disciplinas no momento.\n")
            pass

        elif escolha == 3:  # Eliminar Disciplina

            print("\n3 -  Eliminar Disciplina\n")

            i, flag = 0, 0

            if flag < len(lista_discs): #verificar se existe disciplinas

                disc.mostrarInfo(lista_discs)
                nomeDisc = input("Insira a disciplina a remover nº index ou nome: ")

                if nomeDisc.isalpha(): #caso seja string, executa abaixo. Valida se nome existe e é igual
                    for disc in lista_discs:
                        if nomeDisc == disc.nome_disc:
                            try:
                                lista_discs.pop(i) #apaga por posição, caso seja igual
                                print(f"\nDisciplina {disc.nome_disc} eliminado.\n")
                                disc.mostrarInfo(lista_discs)

                                query = f"delete from disciplinas where nome = '{nomeDisc}' "
                                c.execute(query)
                                db.commit()

                                voltar()
                                break
                            except:
                                print("Erro")
                        i += 1
                        pass
                    else:
                        print(f"\nDisciplina {nomeDisc} não existe no programa.\n")
                        voltar()
                    pass

                elif nomeDisc.isnumeric(): #caso seja int, executa abaixo
                    try:
                        numDisc = int(nomeDisc)

                        #query para eliminar ambos por nome
                        query = f"delete from disciplinas where nome = '{lista_discs[numDisc - 1].nome_disc}' "
                        c.execute(query)
                        db.commit()

                        print("\nDisciplina", lista_discs[numDisc - 1].nome_disc, "eliminado.\n")

                        lista_discs.pop(numDisc - 1)
                        disc.mostrarInfo(lista_discs)
                        voltar()
                        pass
                    except:
                        print(f"\nDisciplina nº {numDisc} nao existe no programa.\n")
                        voltar()
                    pass
            else:
                print(f"Existem {len(lista_discs)} disciplinas no momento.\n")
                voltar()
            pass

        elif escolha == 4:  # Criar Aluno

            print("\n4 - Criar Aluno\n")

            nome = "Insira o primeiro nome: "
            nome_aluno = input_str(nome)

            apelido = "Insira o apelido: "
            apelido_aluno = input_str(apelido)

            idade = "Insira a idade: "
            idade_aluno = input_idade(idade)

            morada_aluno = input("Insira a morada: ")
            cc_aluno = input("Insira o nº do CC/BI: ")

            num = "Insira nº de aluno(a): "

            while True: #valida se existem números iguais
                num_aluno = input_num(num)
                for i in lista_alunos:
                    if num_aluno == i.num_aluno:
                        print(f"\nAluno(a) com o nº {num_aluno} já existe.\n")
                        break
                    else:
                        continue
                else:
                    break

            aluno = Aluno()
            aluno.preencherInfo(nome_aluno, apelido_aluno, idade_aluno, morada_aluno, cc_aluno, num_aluno)
            lista_alunos.append(aluno)

            #query para inserir na BD
            query = f"insert into alunos (nome, apelido_aluno, num_aluno) values ('{nome_aluno}', '{apelido_aluno}', '{num_aluno}')"
            c.execute(query)
            db.commit()

            aluno.InfoCompleta()
            print("\nAluno(a) criado.\n")
            aluno.mostrarInfo(lista_alunos)
            voltar()

        elif escolha == 5:  # Inscrever Aluno

            print("\n5 - Inscrever Aluno\n")

            if len(lista_discs) > 0: #valida se existem disciplinas

                while True: #validar int error
                    try:
                        disc.mostrarInfo(lista_discs)
                        num_disc = int(input("Indique nº index da disciplina: "))
                    except:
                        print("\nInválido\n")
                        continue
                    else:
                        break
                    pass

                if len(lista_alunos) > 0: #valida se existem alunos

                    while True: #validar se já existe alunos inscritos na mesma disciplina
                        try:
                            aluno.mostrarInfo(lista_alunos)
                            aluno_num = int(input("Indique nº index do aluno(a): "))
                            print("")
                            if lista_alunos[aluno_num - 1].num_aluno in lista_discs[num_disc - 1].listaAlunos:
                                print("Aluno(a) já existe nesta disciplina.\n")
                                pass
                            else:
                                # guarda número de aluno na disciplina escolhida
                                lista_discs[num_disc - 1].listaAlunos.append(lista_alunos[aluno_num - 1].num_aluno)
                                print(f"Aluno(a) adicionado à disciplina {lista_discs[num_disc - 1].nome_disc}.\n")
                                pass
                        except:
                            print("Disciplina ou Aluno inválido.\n")
                            print("Certifique-se que escolha apenas disciplinas e alunos existentes.\n")
                            break
                        else:
                            break
                else:
                    print(f"Existem neste momento {len(lista_alunos)} alunos.\n")
                    pass
            else:
                print(f"Existem neste momento {len(lista_discs)} disciplinas e {len(lista_alunos)} alunos.\n")
                pass

        elif escolha == 6:  # Listar Alunos

            print("\n6 - Listar Alunos\n")

            flag = 0

            if flag < len(lista_alunos): #validar se existem alunos
                aluno.mostrarInfo(lista_alunos)
            else:
                print(f"Existem {len(lista_alunos)} alunos no momento\n")
            pass

            voltar()

        elif escolha == 7:  # Eliminar Aluno

            print("\n7 -  Eliminar Aluno\n")

            i, flag = 0, 0

            if flag < len(lista_alunos): #similar ao eliminar disciplina, porém apaga todos os alunos de disciplinas

                aluno.mostrarInfo(lista_alunos)
                nomeAluno = input("Insira o aluno(a) a remover nº index ou primeiro nome: ")

                if nomeAluno.isalpha(): #caso seja string, executa abaixo
                    for aluno in lista_alunos:
                        if nomeAluno == aluno.nome_aluno: #valida se os nomes são iguais
                            try:
                                lista_alunos.pop(i)

                                for inscrito in lista_discs: #validar e apagar alunos de todas as disciplinas

                                    inscrito.apagar(i)

                                print(f"\nAluno(a) {aluno.nome_aluno} eliminado.\n")

                                aluno.mostrarInfo(lista_alunos)

                                query = f"delete from alunos where nome = '{nomeAluno}' "
                                c.execute(query)
                                db.commit()
                                voltar()
                                break

                            except:
                                print("Erro")
                        i += 1
                    else:
                        print(f"\nAluno(a) {nomeAluno} não existe no programa.\n")
                    pass

                elif nomeAluno.isnumeric(): #caso seja int, executa abaixo
                    try:
                        numAluno = int(nomeAluno)

                        for alunos in lista_alunos:
                            try:
                                if lista_alunos[numAluno - 1].nome_aluno == alunos.nome_aluno:

                                    print(f"\nAluno(a) {lista_alunos[numAluno - 1].nome_aluno} eliminado.\n")

                                    query = f"delete from alunos where nome = '{lista_alunos[numAluno - 1].nome_aluno}'"
                                    c.execute(query)
                                    db.commit()

                                    lista_alunos.pop(i)

                                    for inscrito in lista_discs: #validar e apagar alunos de todas as disciplinas

                                        inscrito.apagar(i)

                                    aluno.mostrarInfo(lista_alunos)
                                    voltar()
                                    break
                            except:
                                print(f"\nAluno(a) nº {numAluno} não existe no programa.\n")
                                break
                            i += 1
                    except:
                        continue
                else:
                    print("\nInválido\n")
            else:
                print(f"Existem {len(lista_alunos)} alunos no momento.\n")
            pass

        elif escolha == 8:  # Listar Alunos inscritos numa dadas disciplina

            print("\n8 - Listar Alunos inscritos numa dada disciplina\n")

            flag = 0

            if flag < len(lista_discs):

                disc.mostrarInfo(lista_discs)
                num_disc = int(input("Indique nº index da disciplina: "))

                if len(lista_discs[num_disc - 1].listaAlunos) == 0: #validar se existem alunos inscritos
                    print("\nNão existe alunos inscritos nesta disciplina.\n")
                else:
                    lista_discs[num_disc - 1].verInscritos()
                pass

            else:
                print(f"Existem neste momento {len(lista_discs)} disciplinas e {len(lista_alunos)} alunos.\n")
            pass

            voltar()

        elif escolha == 9:  # Criar Professor

            print("\n9 - Criar Professor\n") #similar ao criar aluno

            nome = "Insira o nome: "
            nome_prof = input_str(nome)

            apelido = "Insira o apelido: "
            apelido_prof = input_str(apelido)

            idade = "Insira a idade: "
            idade_prof = input_idade(idade)

            morada_prof = input("Insira a morada: ")
            catprofi_prof = input("Insira a categoria profissional: ")

            while True: #validar int error
                exp = input("Insira os anos de experiência: ")
                try:
                    anosexp_prof = int(exp)
                    break
                except:
                    print("\nEste campo deve conter apenas números inteiros.\n")
            pass

            num = idade = "Insira nº de professor(a): "

            while True: #valida se exise números iguais
                num_prof = input_num(num)
                for i in lista_profs:
                    if num_prof == i.num_prof:
                        print(f"\nProfessor(a) com o nº {num_prof} já existe.\n")
                        break
                    else:
                        continue
                else:
                    break

            prof = Professor()
            prof.preencherInfo(nome_prof, apelido_prof, idade_prof, morada_prof, catprofi_prof, anosexp_prof, num_prof)
            lista_profs.append(prof)

            #query para inserir valores na BD
            query = f"insert into professores (nome, apelido_prof, num_prof) values ('{nome_prof}', '{apelido_prof}', '{num_prof}')"
            c.execute(query)
            db.commit()

            prof.InfoCompleta() #apenas para confirmar os dados
            print("\nProfessor criado.")
            prof.mostrarInfo(lista_profs) #mostrar lista
            voltar()

        elif escolha == 10:  #Adicionar professor a uma disciplina

            print("\n10 - Adicionar professor a uma disciplina\n")

            flag = 0

            if flag < len(lista_discs) and flag < len(lista_profs): #validar se existe ambos professores e disciplinas

                while True:
                    try:
                        disc.mostrarInfo(lista_discs)
                        num_disc = int(input("Indique o nº index da disciplina: "))

                        #verificar se já existe um professor
                        if len(lista_discs[num_disc - 1].lista_professores) > 0 and len(lista_discs[num_disc - 1].lista_professores) < 2:
                            print("\nJá existe um professor.\n")
                            pass

                        else:
                            prof.mostrarInfo(lista_profs)
                            num_prof = int(input("Indique o nº index do professor(a): "))

                            #guarda professor na disciplina escolhida
                            lista_discs[num_disc - 1].lista_professores.append(lista_profs[num_prof - 1])

                            print(f"\nProfessor nº {num_prof} adicionado a {lista_discs[num_disc - 1].nome_disc}.\n")
                            pass
                    except:
                        print("\nInválido\n")
                        print("Certifique-se que escolha apenas disciplinas e alunos existentes.\n")
                        continue
                    else:
                        break
                    pass
            else:
                print(f"Existem {len(lista_discs)} disciplinas e {len(lista_profs)} professores no momento.\n")
            pass
            voltar()

        elif escolha == 11: #Listar professores

            print("\n11 - Lista de professores para cada disciplina\n")

            flag = 0

            if flag < len(lista_discs): #validar se existe disciplinas

                i = 0

                #Como apenas deverá existir 1 professor por disciplina, é mostrado todos que existam ou não
                for objeto in lista_discs:
                    if len(objeto.lista_professores) == 0:
                        print(f"Disciplina {objeto.nome_disc} - sem professor.\n")
                    else:
                        lista_discs[i].verProfInsc(objeto.nome_disc)
                    i += 1
                pass
            else:
                print(f"Existem neste momento {len(lista_discs)} disciplinas e {len(lista_profs)} professores.\n")
            pass
            voltar()

        elif escolha == 12: #Importacao de ficheiros

            while True: #menu
                try:
                    menu_importar()
                    escolha = int(input("Escolha a opção: "))

                    if escolha == 1: #importa disciplinas, alunos e professores, inclusivé para BD

                        print("\n12 - Importar ficheiro\n")

                        #Alterar path
                        #excel_data_df = pd.read_excel("/Users/felipe/Documents/FelipeSilva_a22100540_ProgII/src/data.xlsx", sheet_name="Folha1")

                        for i in excel_data_df.index:
                            nome_disc = excel_data_df["nome_disc"][i]  # disciplinas

                            nome_aluno = excel_data_df["nome_aluno"][i]  # alunos
                            apelido_aluno = excel_data_df["apelido_aluno"][i]
                            idade_aluno = excel_data_df["idade_aluno"][i]
                            morada_aluno = excel_data_df["morada_aluno"][i]
                            cc_aluno = excel_data_df["cc_aluno"][i]
                            num_aluno = excel_data_df["num_aluno"][i]

                            nome_prof = excel_data_df["nome_prof"][i]  # professores
                            apelido_prof = excel_data_df["apelido_aluno"][i]
                            idade_prof = excel_data_df["idade_prof"][i]
                            morada_prof = excel_data_df["morada_prof"][i]
                            catprofi_prof = excel_data_df["catprofi_prof"][i]
                            anosexp_prof = excel_data_df["anosexp_prof"][i]
                            num_prof = excel_data_df["num_prof"][i]

                            disc = Disciplina()  # disc = disciplina
                            disc.preencherInfo(nome_disc)
                            lista_discs.append(disc)

                            query = f"insert into disciplinas (nome) values ('{nome_disc}')"
                            c.execute(query)
                            db.commit()

                            aluno = Aluno()
                            aluno.preencherInfo(nome_aluno, apelido_aluno, idade_aluno, morada_aluno, cc_aluno, num_aluno)
                            lista_alunos.append(aluno)

                            query = f"insert into alunos (nome, apelido_aluno, num_aluno) values ('{nome_aluno}', '{apelido_aluno}', '{num_aluno}')"
                            c.execute(query)
                            db.commit()

                            prof = Professor()  # prof = professor
                            prof.preencherInfo(nome_prof, apelido_prof, idade_prof, morada_prof, catprofi_prof, anosexp_prof, num_prof)
                            lista_profs.append(prof)

                            query = f"insert into professores (nome, apelido_prof, num_prof) values ('{nome_prof}', '{apelido_prof}', '{num_prof}')"
                            c.execute(query)
                            db.commit()
                            pass

                        print("Ficheiro importado.\n")
                        break
                    pass

                    if escolha == 2: #importa todos os alunos para uma disciplina escolhida

                        print("\n2 - Importar alunos para uma disciplina\n")

                        flag = 0

                        if flag < len(lista_discs) and flag < len(lista_alunos): #valida se existe disciplinas e alunos

                            disc.mostrarInfo(lista_discs)
                            num_disc = int(input("Indique nº index da disciplina: "))
                            print("")

                            #Alterar path
                            #excel_data_df = pd.read_excel("/Users/felipe/Documents/FelipeSilva_a22100540_ProgII/src/data.xlsx", sheet_name="Folha1")

                            for i in excel_data_df.index:

                                num_aluno = excel_data_df["num_aluno"][i]

                                #Guarda número do aluno à disciplina
                                lista_discs[num_disc - 1].listaAlunos.append(lista_alunos[i].num_aluno)

                            aluno.mostrarInfo(lista_alunos)
                            print(f"Alunos inscritos na disciplina {lista_discs[num_disc - 1].nome_disc}.\n")
                            break
                        else:
                            print(f"Existem {len(lista_discs)} disciplinas e {len(lista_alunos)} alunos no momento.\n")
                            voltar()
                            break
                        pass
                except:
                    print("\nOpção inválida")
            pass

        elif escolha == 0:  # Sair do Programa
            print("\nSaiu do programa")
            pass
    except:
        print("\nInválido\n")
        continue
    else:
        pass
