import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def adicionar_contato():
    print("CONTATO ADICIONADO")

def listar_contatos():
    print("LISTA DE CONTATOS")

def editar_contato():
    print("DADOS DO CONTATO")

def lista_favoritos():
    print("LISTA DE CONTATOS FAVORITOS")

def remover_contato():
    print("CONTATO REMOVIDO")


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
            