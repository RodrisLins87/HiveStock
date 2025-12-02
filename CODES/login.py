from CODES.cadastrar import email_valido
from CODES.cadastrar import code_verificação
from CODES.utilits import limpar_tela
from CODES.cadastrar import menu
from CODES.cadastrar import menu_usuario
from CODES.cadastrar import cadastro_usuario
from CODES.utilits import aguardar
import os
import json
import sys
from CODES.cadastro_de_produtos import cadastro_produtos,atualizar_produtos,excluir_produto,listar_produtos_menu,listar_produtos_periodos
from CODES.movimentacao import adicionar_quantidade_prod, retirada_produtos
from CODES.monitoramento import monitoramento
from CODES.relatorio_semana import produto_mais_usado_semana

def fazer_login():
    caminhos_login=["1","2","3","4"]
    tentativas=3

    possibilidade_decisao_funcionario=["1","2","3"]
    possibilidades_menu_login=["1","2",]
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
            ARQUIVO_JSON = os.path.join("Arquivos_JSON", "dados_ADM.json")
        elif tipo_usuario_login == "2":
            ARQUIVO_JSON = os.path.join("Arquivos_JSON", "dados_FUNCIONARIO.json")

        
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
                print("[1] VISUALIZAR PERFIL\n[2] EXCLUIR PERFIL\n[3] AVANÇAR\n[4] SAIR\n")
                escolha_caminho=input("\nSelecione o que deseja:\n ")
                if not escolha_caminho in caminhos_login:
                    print("Valor não é válido")
                    continue

                elif escolha_caminho=="1":
                    limpar_tela()
                    print("Nome:")
                    print(usuario_encontrado['nome'])
                    print("Matrícula:")
                    print(usuario_encontrado['matricula'])
                    print("Email:")
                    print(usuario_encontrado['email'])
                    print("\nPressione ENTER para sair! ")
                    saida=input()
                    if saida=='':
                        print("Saindo...")
                        aguardar(2)
                        limpar_tela()
                        

                elif  escolha_caminho=="2":
                    limpar_tela()
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
                        possibilidade_decisao_adm=["1","2","3","4","5","6","7", "8"]
                        print("[1] CADASTRAR PRODUTO\n[2] VISUALIZAR ESTOQUE\n[3] ATUALIZAR PRODUTOS\n[4] EXCLUIR PRODUTOS\n[5] ADICIONAR QUANTIDADE\n[6] MONITORAMENTO\n[7] RELATORIO_SEMANA\n[8] SAIR")
                        decisao=input("Selecione o que deseja: ")
                        if not decisao in possibilidade_decisao_adm:
                            print("NÃO CONFERE")
                            aguardar(1)
                            limpar_tela
                            continue
                        elif decisao=="1":
                            limpar_tela()
                            cadastro_produtos()
                            aguardar(2)
                            limpar_tela()
                            
                        elif decisao=="2":
                            while 1>0:
                                limpar_tela()
                                print("[1] VISUALIZAR ESTOQUE UNIVERSAL\n[2] VISUALIZAR ESTOQUE POR PERÍODOS\n")
                                possibilidade_visualizar=input("Selecione o que deseja: ")
                                if not possibilidade_visualizar in possibilidades_menu_login:
                                    print("NÃO CONFERE!")
                                    aguardar(2)
                                    limpar_tela()
                                    continue
                                elif possibilidade_visualizar=="1":
                                    limpar_tela()
                                    listar_produtos_menu()
                                    aguardar(3)
                                    limpar_tela()
                                    break 
                                elif possibilidade_visualizar=="2":
                                    limpar_tela()
                                    listar_produtos_periodos()
                                    aguardar(3)
                                    limpar_tela()
                                    break

                        elif decisao=="3":
                            limpar_tela()
                            atualizar_produtos()
                            aguardar(2)
                            limpar_tela()
                            

                        elif decisao=="4":
                            limpar_tela()
                            excluir_produto()
                            aguardar(2)
                            limpar_tela()
                            

                        elif decisao=="5":
                            limpar_tela()
                            adicionar_quantidade_prod()
                            aguardar(2)
                            limpar_tela()

                        elif decisao=="6":
                            limpar_tela()   
                            monitoramento()
                            aguardar(2)
                            limpar_tela()

                        elif decisao=="7":
                            limpar_tela()
                            produto_mais_usado_semana()
                            aguardar(2)
                            limpar_tela()

                        elif decisao=="8":
                            print("Saindo")
                            aguardar(2)
                            limpar_tela()
                            break
                            

                      

                elif escolha_caminho=="3" and tipo_usuario_login=="2":
                    print("Carregando...")
                    aguardar(3)
                    limpar_tela()
                    while 1>0:
                        print("[1] VISUALIZAR PRODUTOS\n[2] RETIRAR QUANTIDADE\n[3] SAIR")
                        escolha_funcionario=input("Selecione o que deseja: ")
                        if not escolha_funcionario in possibilidade_decisao_funcionario:
                            print("NÃO É VÁLIDO!")
                            aguardar(3)
                            limpar_tela()
                            continue 

                        elif escolha_funcionario=="1":
                            while 1>0:
                                limpar_tela()
                                alternativas_visualizar_funcionario=["1","2","3"]
                                print("[1] VISUALIZAR TODOS OS PRODUTOS\n[2] VISUALIZAR POR PERÍODOS\n[3] SAIR")
                                escolha_visualizar=input("Selecione o que deseja: ")
                                if not escolha_visualizar in alternativas_visualizar_funcionario:
                                    print("NÃO CONFERE!")
                                    aguardar(3)
                                    limpar_tela()
                                    continue
                                elif escolha_visualizar=="1":
                                    limpar_tela()
                                    listar_produtos_menu()
                                    aguardar(3)
                                    limpar_tela()
                                    
                                    
                                elif escolha_visualizar=="2":
                                    limpar_tela()
                                    listar_produtos_periodos()
                                    aguardar(3)
                                    limpar_tela()
                                    

                                elif escolha_visualizar=="3":
                                    aguardar(2)
                                    limpar_tela()
                                    break
                                    

                        elif escolha_funcionario=="2":
                            limpar_tela()
                            retirada_produtos()
                            aguardar(3)
                            limpar_tela()

                        

                        elif escolha_funcionario=="3":
                            print("Saindo...")
                            aguardar(2)
                            limpar_tela()
                            break


                elif escolha_caminho=="4":
                    print("Saindo...3,2,1")
                    aguardar(3)
                    limpar_tela()
                    return




        else:
            tentativas -= 1
            print("❌ Usuário ou senha incorretos!")
            aguardar(2)
            limpar_tela()
            return


    

