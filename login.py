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
from cadastro_de_produtos import cadastro_produtos,atualizar_produtos,excluir_produto,listar_produtos_menu,listar_produtos_periodos
from alteracao_quantidade import adicionar_quantidade_prod, retirada_produtos
from aviso_estoque import monitoramento

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

                elif escolha_caminho=="3" and tipo_usuario_login=="1":
                    print("Carregando...")
                    aguardar(3)
                    limpar_tela()
                    while 1>0:
                        possibilidade_decisao=["1","2","3","4","5","6","7"]
                        print("[1] CADASTRAR PRODUTO\n[2] VISUALIZAR ESTOQUE\n[3] ATUALIZAR PRODUTOS\n[4] EXCLUIR PRODUTOS\n[5] ADICIONAR QUANTIDADE\n[6] MONITORAMENTO\n [7] SAIR")
                        decisao=input("Selecione o que deseja: ")
                        if not decisao in possibilidade_decisao:
                            print("NÃO CONFERE")
                            aguardar(1)
                            limpar_tela
                            continue
                        elif decisao=="1":
                            cadastro_produtos()
                            aguardar(2)
                            limpar_tela
                            
                        elif decisao=="2":
                            while 1>0:
                                print("[1] VISUALIZAR ESTOQUE UNIVERSAL\n[2] VISUALIZAR ESTOQUE POR PERÍODOS\n")
                                possibilidade_visualizar=input("Selecione o que deseja: ")
                                if not possibilidade_visualizar in possibilidades_menu_login:
                                    print("NÃO CONFERE!")
                                    aguardar(2)
                                    limpar_tela()
                                    continue
                                elif possibilidade_visualizar=="1":
                                    listar_produtos_menu()
                                    aguardar(3)
                                    limpar_tela()
                                    break 
                                elif possibilidade_visualizar=="2":
                                    listar_produtos_periodos()
                                    aguardar(3)
                                    limpar_tela()
                                    break

                        elif decisao=="3":
                            atualizar_produtos()
                            aguardar(2)
                            limpar_tela()
                            

                        elif decisao=="4":
                            excluir_produto()
                            aguardar(2)
                            limpar_tela()
                            

                        elif decisao=="5":
                            adicionar_quantidade_prod()
                            aguardar(2)
                            limpar_tela()

                        elif decisao=="6":
                            monitoramento()
                            aguardar(2)
                            limpar_tela()

                        elif decisao=="7":
                            return
                            

                      

                elif escolha_caminho=="3" and tipo_usuario_login=="2":
                    print("Carregando...")
                    aguardar(3)
                    limpar_tela()
                    while 1>0:
                        print("[1] VISUALIZAR PRODUTOS\n[2]RETIRAR QUANTIDADE\n")
                        escolha_funcionario=input("Selecione o que deseja: ")
                        if not escolha_funcionario in possibilidades_menu_login:
                            print("NÃO É VÁLIDO!")
                            aguardar(3)
                            limpar_tela()
                            continue 

                        elif escolha_funcionario=="1":
                            while 1>0:
                                alternativas_visualizar_funcionario=["1","2","3"]
                                print("[1] VISUALIZAR TODOS OS PRODUTOS\n[2] VISUALIZAR POR PERÍODOS\n [3] SAIR")
                                escolha_visualizar=input("Selecione o que deseja: ")
                                if not escolha_visualizar in alternativas_visualizar_funcionario:
                                    print("NÃO CONFERE!")
                                    aguardar(3)
                                    limpar_tela()
                                    continue
                                elif escolha_visualizar=="1":
                                    listar_produtos_menu()
                                    aguardar(3)
                                    limpar_tela()
                                    
                                    
                                elif escolha_visualizar=="2":
                                    listar_produtos_periodos()
                                    aguardar(3)
                                    limpar_tela()
                                    

                                elif escolha_visualizar=="3":
                                    return
                                    

                        elif escolha_funcionario=="2":
                            retirada_produtos()
                            aguardar(3)
                            limpar_tela()

                        

                        elif escolha_funcionario=="4":
                            return


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
            return


    

