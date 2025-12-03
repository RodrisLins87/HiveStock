import json
import os
from datetime import datetime
from CODES.utilits import aguardar,limpar_tela, arquivo
from CODES.produto import Produto


def carregar_produtos():
    try:
        with open(arquivo, "r",) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:                                                                             # caso o arquivo não exista
        return []  
    
def salvar_produtos(produtos):
    with open(arquivo, "w") as escrita:
        json.dump(produtos, escrita, indent= 4)

def cadastro_produtos():
    produtos = carregar_produtos()
    agora = datetime.now() 
    data_atual = agora.strftime("%d/%m/%Y")
    mes_ano = agora.strftime("%m/%Y")

    while True:
        tipo = input("Digite o tipo do seu produto: ").strip().lower()
        nome_produto = input("Digite o nome do produto que vai ser cadastrado: ").strip().lower()

        while True:
            try:
                quantidade = int(input("Informe a quantidade: "))
                break
            except ValueError:
                print("⚠️ Digite um valor válido. Apenas números serão aceitos ⚠️")

        while True:
            try:
                nota_fiscal = int(input("Informe a Nota Fiscal: "))
                break
            except ValueError:
                print("⚠️ Digite um valor válido. Apenas números serão aceitos ⚠️")

        for produto in produtos:
            if produto["NF"] == nota_fiscal and produto["Nome"] == nome_produto:
                print("Essa produto já foi cadastrado")
                aguardar(2)
                limpar_tela()
                return

        produto = Produto(tipo, nome_produto, quantidade, nota_fiscal, data_atual, mes_ano).to_dict()

        produtos = carregar_produtos()
        produtos.append(produto)
        salvar_produtos(produtos)
        print("produto cadastrado com sucesso")
        
        while True:
            entrada = input("Deseja cadastrar mais um produto? (s/n): ").strip().lower()

            if entrada == "s":
                aguardar(2)
                limpar_tela()
                break
            elif entrada == "n":
                print("Saindo...\n")
                aguardar(2)
                limpar_tela()
                return
            else:
                limpar_tela()
                print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não.")
                continue

def listar_produtos_menu():
    produtos = carregar_produtos()
    if not produtos:                                                                                                                        #Lista todos os produtas já cadastrados
        print("Não existem produtos cadastrados")
        aguardar(2)
        limpar_tela()
        return                                                                              
    
    for i,a in enumerate(produtos, start = 1):
        print(f"{i}. Tipo: {a["Tipo"]} | Nome: {a["Nome"]} | Quant: {a["Quantidade"]} | Nota fiscal: {a["NF"]}")
    print("Pressione ENTER para sair")
    entrada = input()
    if entrada == "":
        print("Saindo...")
        return
    
def listar_produtos():
    produtos = carregar_produtos()
    if not produtos:                                                                                                                        #Lista todos os produtas já cadastrados
        print("Não existem produtos cadastrados")
        aguardar(2)
        limpar_tela()
        return                                                                              
    
    for i,a in enumerate(produtos, start = 1):
        print(f"{i}. Tipo: {a["Tipo"]} | Nome: {a["Nome"]} | Quant: {a["Quantidade"]} | Nota fiscal: {a["NF"]}")

def listar_produtos_periodos():
    produtos = carregar_produtos()

    
    if not produtos:
        print("Não existem produtos cadastrados.")
        return

    while True:
        print("""
            1 - Jan
            2 - Fev
            3 - Mar
            4 - Abr
            5 - Mai
            6 - Jun
            7 - Jul
            8 - Ago
            9 - Set
            10 - Out
            11 - Nov
            12 - Dez
        """)

    # --- Tratamento de entrada do mês ---
        try:
            mes_int = int(input("Escolha o mês de análise (1 a 12): ").strip())
            if mes_int < 1 or mes_int > 12:
                limpar_tela()                                                                             # Verifica se a entrada é número
                print("⚠️ Entrada inválida! Digite apenas números de 1 a 12. ⚠️")
                continue
        except ValueError:
            limpar_tela()
            print("⚠️ Entrada inválida! Digite apenas números de 1 a 12. ⚠️")
            continue

        aguardar(2)
        limpar_tela()
        
        print("Carregando produtos...")
        aguardar(2)
        limpar_tela()

        mes = str(mes_int).zfill(2)                                                                         # converte para str e converte para formato 2 dígitos (01, 02, ...)
        

        produtos_do_mes = [p for p in produtos if p["mes_ano"] == f"{mes}/2025"]                                # Percorre a lista de produtos, filtrando apenas pelo mês digitado
        
        if not produtos_do_mes:                                                                                 # Verifica se existem produtos cadastrados no mês informado    
            print(f"📅 Não existem produtos cadastrados no período {mes}/2025.")
            
        else:
            print(f"\n📦 Produtos cadastrados em {mes}/2025:\n")
            for i, a in enumerate(produtos_do_mes, start=1):
                print(f"{i}. Tipo: {a['Tipo']} | Nome: {a['Nome']} | Quant: {a['Quantidade']} | Nota fiscal: {a['NF']}")
            
        while True:
                entrada = input("Deseja verificar mais algum periodo? (s/n): ").strip().lower()

                if entrada == "s":
                    aguardar(2)
                    limpar_tela()
                    break
                elif entrada == "n":
                    print("Saindo...\n")
                    aguardar(2)
                    limpar_tela()
                    return
                else:
                    limpar_tela()
                    print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não. ⚠️")
                    continue

def atualizar_produtos():
    produtos = carregar_produtos()
    while True:
        if not produtos:
            print("Nenhum produto cadastrado para atualizar.")                                          #Para caso não haja nenhum produto cadastrado
            return

        listar_produtos()                                                                               #Lista para o usuario se basear         

        try:
            indice = int(input("Digite o número do produto que deseja atualizar: ")) - 1                #O usuário colocará o indice que a aparecer na lista, porém o python lê o primeiro com 0
            if indice < 0 or indice >= len(produtos):     
                limpar_tela()                                              #Vê se o usuário coloco um indice válido
                print("⚠️ Índice inválido. ⚠️")
                continue
        except ValueError:
            limpar_tela()
            print("⚠️ Entrada inválida. Digite um número. ⚠️")
            continue

        aguardar(2)
        limpar_tela()

        while True:
            print("""
        Qual campo você deseja alterar?
        1 - Tipo
        2 - Nome
        3 - Quantidade
        4 - Nota Fiscal
        0 - Sair
        """)

        
            try:
                campo = int(input("Escolha uma opção (1-4): "))
                if campo < 0 or campo > 4:
                    limpar_tela()
                    print("⚠️ Opção inválida. escolha um numero entre 0 e 4. ⚠️")
                    continue
            except ValueError:
                limpar_tela()
                print("⚠️ Entrada inválida. Somente números são permitidos. ⚠️")
                continue

            if campo == 1:
                novo_valor = input("Digite o novo tipo: ")
                produtos[indice]["Tipo"] = novo_valor                               #armazena o novo valor na lista de produto, pega o vai diretamente no indice que o user digitou e muda some o campo escolhido
            elif campo == 2:
                novo_valor = input("Digite o novo nome: ")
                produtos[indice]["Nome"] = novo_valor
            elif campo == 3:
                try:
                    novo_valor = int(input("Digite a nova quantidade: "))
                except ValueError:
                    print("⚠️ Quantidade inválida. Digite apenas números. ⚠️")
                    aguardar(2)
                    limpar_tela()
                    continue
                if novo_valor < 0 or novo_valor > 500:
                    print("⚠️ Digite uma quantidade válida entre 0 e 500. ⚠️")
                    aguardar(2)
                    limpar_tela()
                    continue
                else:    
                    produtos[indice]["Quantidade"] = novo_valor
                
            elif campo == 4:
                try:
                    novo_valor = int(input("Digite a nova Nota Fiscal: "))
                    produtos[indice]["NF"] = novo_valor
                except ValueError:
                    print("⚠️ Nota fiscal inválida. ⚠️")
                    return
            elif campo == 0:
                return
            else:
                print("⚠️ Opção inválida. ⚠️")
                return

            aguardar(2)
            limpar_tela()
            salvar_produtos(produtos)
            print("✅ Produto atualizado com sucesso! ✅")
            listar_produtos()

            while True:
                entrada = input("Deseja atualizar mais algum periodo? (s/n): ").strip().lower()

                if entrada == "s":
                    sair = True
                    aguardar(2)
                    limpar_tela()
                    break
                elif entrada == "n":
                    print("Saindo...\n")
                    aguardar(2)
                    limpar_tela()
                    return
                else:
                    limpar_tela()
                    print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não.")
                    continue

            if sair:
                sair = False
                break

    
def excluir_produto():
    produtos = carregar_produtos()
    if not produtos:
        print("Não existem produtos cadastrados")
        return  
    while True: 
        listar_produtos()
        
        try:
            indice = int(input("Digite o indice do produto que você quer excluir")) - 1
            if indice < 0 or indice >= len(produtos):
                limpar_tela()
                print("⚠️ Indice invalido ⚠️")
                continue
        except ValueError:
            limpar_tela()
            print("⚠️ Entrada inválida. Digite um número. ⚠️")
            continue
        
        entrada = input("Prissionando ENTER, confirme a exclusão ou digite qualquer outra coisa para cancelar a operação  ")
        if entrada != '':
            print("Operação cancelada ❌")
            return
        else:
            produtos.pop(indice)
            print("✅ Produto removido com sucesso ✅")
            aguardar(2)
            limpar_tela()
        salvar_produtos(produtos)
        listar_produtos()
        print("Pressione ENTER para sair")
        entrada = input()
        if entrada == "":
            print("Saindo...")
            return

#cadastro_produtos()
#listar_produtos()
#listar_produtos_periodos()
#atualizar_produtos()
#excluir_produto()
