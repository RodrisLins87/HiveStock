from cadastrar import menu
from cadastrar import menu_usuario
from cadastrar import cadastro_usuario
from cadastrar import limpar_tela
from cadastrar import aguardar
from login import fazer_login
from recuperacao import recuperar_senha
from recuperacao import buscar_usuario_por_email
from recuperacao_adm import buscar_usuario_por_email_ADM
from recuperacao_adm import recuperar_senha_ADM

escolhas_login = ["1", "2", "3", "4"]
possibilidades_cadastro = ["1", "2"]

while 1>0:
    limpar_tela()
    menu()  
    entrada_1 = input("Selecione o que deseja: ").strip()

    if entrada_1 not in escolhas_login:
        print("Valor não confere! Tente novamente.\n")
        aguardar(2)
        continue

    elif entrada_1 == "1":
        print("Vamos criar seu cadastro!")
        aguardar(2)
        limpar_tela()
        cadastro_usuario()
        break

    elif entrada_1 == "2":
        print("Vamos fazer o login!")
        aguardar(2)
        limpar_tela()
        fazer_login()

    elif entrada_1 == "3":
        while 1>0:
            limpar_tela()
            print("[1] FUNCIONÁRIO\n[2] ADMINISTRADOR")
            escolha_recuperacao = input("Qual é o tipo da sua conta? ").strip()

            if escolha_recuperacao not in ["1", "2"]:
                print("Opção inválida! Tente novamente.")
                aguardar(2)
                continue

            elif escolha_recuperacao=="1":
                print("Carregando...")
                aguardar(2)
                limpar_tela()
                recuperar_senha()
                break  

            else:
                print("Carregando...")
                aguardar(2)
                limpar_tela()
                recuperar_senha_ADM()
                break

    elif entrada_1 == "4":
        print("Saindo do sistema...")
        aguardar(2)
        break  

            
    



       