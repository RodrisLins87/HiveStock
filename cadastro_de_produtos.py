import json
import time
import os
from datetime import datetime

arquivo = "produtos.json"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')



def carregar_produtos():
    try:
        with open(arquivo, "r",) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Arquivo vazio ou inválido, carregando uma nova lista")
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
                print("Digite um valor válido")

        while True:
            try:
                nota_fiscal = int(input("Informe a Nota Fiscal: "))
                break
            except ValueError:
                print("Digite um valor válido")

        for produto in produtos:
            if produto["NF"] == nota_fiscal and produto["Nome"] == nome_produto:
                print("Essa produto já foi cadastrado")
                time.sleep(2)
                limpar_tela()
                return
        produto = {"Tipo": tipo, "Nome" : nome_produto, "Quantidade": quantidade, "NF" : nota_fiscal, "data_inclusao" : data_atual, "mes_ano":mes_ano}
        produtos = carregar_produtos()
        produtos.append(produto)
        salvar_produtos(produtos)
        print("produto cadastrado com sucesso")
        
        while True:
            entrada = input("Deseja cadastrar mais um produto? (s/n): ").strip().lower()

            if entrada == "s":
                time.sleep(2)
                limpar_tela()
                break
            elif entrada == "n":
                print("Encerrando cadastro de produtos...\n")
                time.sleep(2)
                limpar_tela()
                return
            else:
                print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não.")

def listar_produtos_menu():
    produtos = carregar_produtos()
    if not produtos:                                                                                                                        #Lista todos os produtas já cadastrados
        print("Não existem produtos cadastrados")
        time.sleep(2)
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
        time.sleep(2)
        limpar_tela()
        return                                                                              
    
    for i,a in enumerate(produtos, start = 1):
        print(f"{i}. Tipo: {a["Tipo"]} | Nome: {a["Nome"]} | Quant: {a["Quantidade"]} | Nota fiscal: {a["NF"]}")

def listar_produtos_periodos():
    produtos = carregar_produtos()

    if not produtos:
        print("⚠️ Não existem produtos cadastrados.")
        return

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
    while True:
        mes = input("Escolha o mês de análise (1 a 12): ").strip()

        if not mes.isdigit():                                                                               # Verifica se a entrada é número
            print("⚠️ Entrada inválida! Digite apenas números de 1 a 12.")
            continue

        mes_int = int(mes)

        time.sleep(2)
        limpar_tela()
        if mes_int < 1 or mes_int > 12:                                                                     # Verifica se o número está dentro do intervalo válido        
            print("⚠️ Mês inválido! Digite um número entre 1 e 12.")
            continue

        print("Carregando produtos...")
        time.sleep(2)
        limpar_tela()

        mes = str(mes_int).zfill(2)                                                                         # converte para str e converte para formato 2 dígitos (01, 02, ...)
        break

    produtos_do_mes = [p for p in produtos if p["mes_ano"] == f"{mes}/2025"]                                # Percorre a lista de produtos, filtrando apenas pelo mês digitado
    
    if not produtos_do_mes:                                                                                 # Verifica se existem produtos cadastrados no mês informado    
        print(f"📅 Não existem produtos cadastrados no período {mes}/2025.")
        return

    print(f"\n📦 Produtos cadastrados em {mes}/2025:\n")
    for i, a in enumerate(produtos_do_mes, start=1):
        print(f"{i}. Tipo: {a['Tipo']} | Nome: {a['Nome']} | Quant: {a['Quantidade']} | Nota fiscal: {a['NF']}")
    print("Pressione ENTER para sair")
    entrada = input()
    if entrada == "":
        print("Saindo...")
        return

def atualizar_produtos():
    produtos = carregar_produtos()
    while True:
        if not produtos:
            print("Nenhum produto cadastrado para atualizar.")                                          #Para caso não haja nenhum produto cadastrado
            return

        listar_produtos()                                                                               #Lista para o usuario se basear         

        try:
            indice = int(input("Digite o número do produto que deseja atualizar: ")) - 1                #O usuário colocará o indice que a aparecer na lista, porém o python lê o primeiro com 0
            if indice < 0 or indice >= len(produtos):                                                   #Vê se o usuário coloco um indice válido
                print("Índice inválido.")
                return
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return

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
        except ValueError:
            print("Entrada inválida.")
            return

        if campo == 1:
            novo_valor = input("Digite o novo tipo: ")
            produtos[indice]["Tipo"] = novo_valor                               #armazena o novo valor na lista de produto, pega o vai diretamente no indice que o user digitou e muda some o campo escolhido
        elif campo == 2:
            novo_valor = input("Digite o novo nome: ")
            produtos[indice]["Nome"] = novo_valor
        elif campo == 3:
            try:
                novo_valor = int(input("Digite a nova quantidade: "))
                produtos[indice]["Quantidade"] = novo_valor
            except ValueError:
                print("Quantidade inválida.")
                return
        elif campo == 4:
            try:
                novo_valor = int(input("Digite a nova Nota Fiscal: "))
                produtos[indice]["NF"] = novo_valor
            except ValueError:
                print("Nota fiscal inválida.")
                return
        elif campo == 0:
            return
        else:
            print("Opção inválida.")
            return

        salvar_produtos(produtos)
        print("Produto atualizado com sucesso!")
        listar_produtos()

        while True:
                entrada = input("Deseja cadastrar mais um produto? (s/n): ").strip().lower()

                if entrada == "s":
                    time.sleep(2)
                    limpar_tela()
                    break
                elif entrada == "n":
                    print("Saindo...\n")
                    time.sleep(2)
                    limpar_tela()
                    return
                else:
                    print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não.")

def excluir_produto():
    produtos = carregar_produtos()
    if not produtos:
        print("Não existem produtos cadastrados")
        return  
    
    listar_produtos()
    
    try:
        indice = int(input("Digite o indice do produto que você quer excluir")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Indice invalido")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return
    
    entrada = input("Prissionando ENTER, confirme a exclusão ou digite qualquer outra coisa para cancelar a operação  ")
    if entrada != '':
        print("Operação cancelada")
        return
    else:
        produtos.pop(indice)
        print("Produto removido com sucesso")
        time.sleep(2)
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
