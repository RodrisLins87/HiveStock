from cadastrar import email_valido
from cadastrar import code_verificação
from cadastrar import limpar_tela
from cadastrar import menu
from cadastrar import menu_usuario
from cadastrar import cadastro_usuario
from cadastrar import aguardar
import os
import json
import sys

def fazer_login():
    caminhos_login=["1","2","3","4"]
    tentativas=3

    possibilidades_menu_login=["1","2"]
    print("Vamos fazer o login!")
    aguardar(1)
    limpar_tela()

    email_login=input("Qual o email? ")
    print("Carregando...")
    aguardar(1)
    limpar_tela()

    senha_login=input("Qual a senha? ")
    print("Carregando...")
    aguardar(1)
    limpar_tela()
    
    
    while tentativas > 0:
        menu_usuario()
        tipo_usuario_login = input("Selecione o tipo de conta: ")

        if tipo_usuario_login not in possibilidades_menu_login:
            print("❌ Opção não encontrada!")
            aguardar(1)
            limpar_tela()
            continue

        
        if tipo_usuario_login == "1":
            ARQUIVO_JSON = "dados_ADM.json"
        elif tipo_usuario_login == "2":
            ARQUIVO_JSON = "dados_FUNCIONARIO.json"

        
        if not os.path.exists(ARQUIVO_JSON):
            print("⚠️ Nenhum usuário cadastrado ainda!")
            aguardar(2)
            limpar_tela()
            menu()
            return

        
        with open(ARQUIVO_JSON, "r") as f:
            dados = json.load(f)

        
        usuario_encontrado = None

        
        for u in dados["usuarios"]:
            if u.get("email") == email_login and u.get("senha") == senha_login:
                usuario_encontrado = u
                break

        
        if usuario_encontrado:
            print(f"✅ Seja bem-vindo, {usuario_encontrado['nome']}!")
            aguardar(3)
            limpar_tela()
            while 1>0:  
                print("[1] VISUALIZAR PERFIL\n[2] EXCLUIR PERFIL\n[3] AVANÇAR\n[4] SAIR")
                escolha_caminho=input("Selecione o que deseja: ")
                if not escolha_caminho in caminhos_login:
                    print("Valor não é válido")
                    continue

                elif escolha_caminho=="1":
                    print("Nome:")
                    print(usuario_encontrado['nome'])
                    print("Matrícula:")
                    print(usuario_encontrado['matricula'])
                    print("Email:")
                    print(usuario_encontrado['email'])
                    break

                elif  escolha_caminho=="2":
                    print("[1] SIM\n[2] NÃO")
                    while 1>0:
                        certeza=input("Tem certeza que quer excluir o perfil? ")
                        if not certeza in possibilidades_menu_login:
                            print("NÃO CONFERE!")
                            continue

                        elif certeza=="1":
                            with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
                                dados = json.load(f)
                                usuarios = dados["usuarios"]

                                # Remove o usuário que tem o email correspondente, ignorando dicionários sem a chave
                                usuarios = [u for u in usuarios if isinstance(u, dict) and u.get("email") != email_login]

                                # Atualiza o dicionário e salva
                                dados["usuarios"] = usuarios
                                with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
                                    json.dump(dados, f, indent=4, ensure_ascii=False)

                                print("Perfil excluído com sucesso!")
                                print("Saindo...3,2,1")
                                aguardar(3)
                                limpar_tela()
                                sys.exit
                                break


                        elif certeza=="2":
                            print("Cancelando...")
                            aguardar(3)
                            limpar_tela()
                            sys.exit()

                        else:
                            break

                elif escolha_caminho=="3":
                    print("Carregando...")
                    aguardar(3)
                    limpar_tela()
                    break

                elif escolha_caminho=="4":
                    print("Saindo...3,2,1")
                    aguardar(3)
                    limpar_tela()
                    sys.exit()
                    break 




        else:
            tentativas -= 1
            print("❌ Usuário ou senha incorretos!")
            aguardar(2)
            limpar_tela()
            break


    print("⚠️ Tentativas esgotadas! Saindo...")
    aguardar(2)
    limpar_tela()
    sys.exit()

