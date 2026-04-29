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
    print("\n" + "=" * 50)
    print("✅ CONTATO ADICIONADO COM SUCESSO!".center(50))
    print("=" * 50)
    # print(agenda)

def listar_contatos():
    print("\n" + "=" * 50)
    print("📋 LISTA DE CONTATOS".center(50))
    print(f"\n📊 TOTAL DE CONTATOS: {len(agenda)}")
    print("=" * 50)

    if not agenda:
        print("\n⚠️ Nenhum contato cadastrado.")
        print("=" * 50)
        return

    for contato in agenda:

        favorito_icon = "⭐" if contato["Favoritos"] else ""

        print(f"\n🆔 ID: {contato['IP']} {favorito_icon}")
        print("-" * 50)

        print(f"👤 Nome      : {contato['Contato']}")
        print(f"📞 Telefone : {contato['Telefone']}")
        print(f"📧 Email    : {contato['Email']}")
        print(f"⭐ Favorito : {'Sim' if contato['Favoritos'] else 'Não'}")

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

        print("\n" + "=" * 50)
        print("✏️ CONTATO ATUALIZADO COM SUCESSO!".center(50))
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("❌ CONTATO NÃO ENCONTRADO!".center(50))
        print("=" * 50)

def lista_favoritos():
    print("\n" + "=" * 50)
    print("⭐ CONTATOS FAVORITOS".center(50))
    print("=" * 50)

    encontrou = False

    for contato in agenda:

        if contato["Favoritos"]:

            encontrou = True

            print(f"\n🆔 ID: {contato['IP']}")
            print("-" * 50)

            print(f"👤 Nome      : {contato['Contato']}")
            print(f"📞 Telefone : {contato['Telefone']}")
            print(f"📧 Email    : {contato['Email']}")

            print("=" * 50)

    if not encontrou:
        print("\n⚠️ Nenhum contato favorito encontrado.")
        print("=" * 50)

def remover_contato():
    listar_contatos()
    ip = int(input("\nDigite o ID do contato para remover: "))
    for contato in agenda:
        if contato["IP"] == ip:
            agenda.remove(contato)

    print("\n" + "=" * 50)
    print("🗑️ CONTATO REMOVIDO COM SUCESSO!".center(50))
    print("=" * 50)

def mostrar_menu():
    print("=" * 50)
    print("📒  AGENDA INTELIGENTE PYTHON".center(50))
    print("=" * 50)

    print("\nSelecione uma opção:\n")

    print(" [1] ➕  Adicionar contato")
    print(" [2] 📋  Listar contatos")
    print(" [3] 🔍  Editar contato")
    print(" [4] ⭐   Listar favoritos")
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
            