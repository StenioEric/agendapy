import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
agenda = []
def adicionar_contato():
    # Funcionalidade de adicionar contatos e favoritar
    ip = len(agenda) + 1
    nome = input("\n Digite seu nome: ")
    tel = input("\n Digite seu telefone: ")
    email = input("\n Digite seu email: ")
    favoritos = input("\n Adicionar número aos favoritos(SIM/NÃO): ")

    if favoritos == "SIM":
        favoritos = True
    else:
        favoritos = False

    contato = {"Contato": nome,
               "Telefone":tel,
               "Email":email,
               "Favoritos": favoritos,
               "IP": ip,
               }
    
    agenda.append(contato)
    print("\n CONTATO ADICIONADO")
    # print(agenda)

def listar_contatos():
    print("LISTA DE CONTATOS")

    for contato in agenda:
        for chave, valor in contato.items():
            print(chave, ":" , valor,)
        print("=" * 50)

def editar_contato():

    listar_contatos()
    ip = int(input("\nDigite o ID do contato para editar: "))
    opcao = input("\nDigite a opção de edição: \n [1] Editar nome \n [2] Editar telefone \n [3] Editar email \n [4] Editar favoritos \n [5] Editar tudo \n")
    indice_contato = ip - 1

    if indice_contato >= 0 and indice_contato < len(agenda):

        match opcao:
            case "1":                
                newName = input("Digite o novo nome: ")
                agenda[indice_contato]["Contato"] = newName
            case "2":
                newFone = input("Digite o novo número: ")
                agenda[indice_contato]["Telefone"] = newFone
            case "3":
                newEmail = input("Digite o novo email: ")
                agenda[indice_contato]["Email"] = newEmail
            case "4":
                newFavoritos = input("Digite 1 para favoritar e 0 para remover dos favoritos: ")
                if newFavoritos == "1":
                    agenda[indice_contato]["Favoritos"] = True
                else:            
                    agenda[indice_contato]["Favoritos"] = False
            case "5":
                newName = input("Digite o novo nome: ")
                newFone = input("Digite o novo número: ")
                newEmail = input("Digite o novo email: ")
                newFavoritos = input("Digite 1 para favoritar e 0 para remover dos favoritos: ")

                agenda[indice_contato]["Contato"] = newName
                agenda[indice_contato]["Telefone"] = newFone
                agenda[indice_contato]["Email"] = newEmail

                if newFavoritos == "1":
                    agenda[indice_contato]["Favoritos"] = True
                else:            
                    agenda[indice_contato]["Favoritos"] = False

        print("\nContato atualizado com sucesso!")
    else:
        print("\nContato inválido!")


def lista_favoritos():
    print("\n LISTA DE CONTATOS FAVORITOS")
    for contato in agenda:
        if contato["Favoritos"] == True:
            for chave, valor in contato.items():
                print(chave, ":" , valor,)
            print("\n" + "=" * 50)

def remover_contato():
    listar_contatos()
    ip = int(input("\nDigite o ID do contato para remover: "))
    for contato in agenda:
        if contato["IP"] == ip:
            agenda.remove(contato)

    print("\n CONTATO REMOVIDO")

def mostrar_menu():
    print("=" * 50)
    print("📒  AGENDA INTELIGENTE PYTHON".center(50))
    print("=" * 50)

    print("\nSelecione uma opção:\n")

    print(" [1] ➕  Adicionar contato")
    print(" [2] 📋  Listar contatos")
    print(" [3] 🔍  Editar contato")
    print(" [4] 🔍  Listar favoritos")
    print(" [5] ❌  Remover contato")
    print(" [0] 🚪  Sair")

    print("\n" + "=" * 50)

while True:
    limpar_tela()
    mostrar_menu()
    ip = 0

    opcao = input("Digite o número da sua opoção: ")

    match opcao:
        case "1":
            adicionar_contato()
        case "2":
            listar_contatos()
        case "3":
            editar_contato()
        case "4":
            lista_favoritos()
        case "5":
            remover_contato()
        case "0":
            break


    time.sleep(3)
            