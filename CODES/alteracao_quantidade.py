import json
import time
import os
from datetime import datetime
from CODES.cadastro_de_produtos import listar_produtos, carregar_produtos,salvar_produtos
from CODES.utilits import aguardar, limpar_tela

arquivo = "produtos.json"


def adicionar_quantidade_prod():
    produtos = carregar_produtos()
    
    while True:
        if not produtos:
            print("Não existem produtos cadastrados")
            return

        listar_produtos()

        try:
            print("Digite o indice do produto que você deseja adicionar na quantidade do estoque")
            indice = int(input())-1
            if indice < 0 or indice > len(produtos)-1:
                print("Digite um valor valido")
                return
        except ValueError:
            print("Digite um valor válido. Apenas números serão aceitos")
            return
        

        try:
            quantidade = int(input("Digite a quantidade: \n"))
            if quantidade <= 0 or quantidade > 500:
                print("Digite uma quantidade valida. (numeros negativos, nem maiores que 500 serão aceitos.")
                return
        except ValueError:
            print("Digite uma valor valido. Apenas números serão aceitos")
            return
        
        print("Aguarde...")
       
        produtos[indice]["Quantidade"] += quantidade                                                                #Soma com a quant antiga
        
        salvar_produtos(produtos)
        print("Produto atualizado com sucesso!")
        listar_produtos()

        while True:
            entrada = input("Deseja adicionar mais algum produto? (s/n): ").strip().lower()

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
                print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não.")

def retirada_produtos():
    produtos = carregar_produtos()
    while True:
        
        if not produtos:
            print("Não existem produtos cadastrados.")
            return

        listar_produtos()

        try:
            print("Digite o indice do produto que você quer retirar")
            indice = int(input())-1
            comprimento = len(produtos)
            if indice < 0 or indice+1 > comprimento:
                print(f"Digite um valor valido. Não serão aceitos numeros maiores que {comprimento}")
                return
        except ValueError:
            print("Digite um valor valido. Só serão aceitos numeros")
            return
        

        quantidade = int(input("Digite a quantidade a ser retirada\n"))

        try:
            if quantidade <= 0 or quantidade > produtos[indice]["Quantidade"]:
                print("Digite um valor valido. Numeros negativos não serão aceitos, nem um valor superior a quantidade atual.")
                return
        except ValueError:
            print("Digite um valor valido. Só serão aceitos numeros")
            return
        
        print("Aguarde...")

        produtos[indice]["Quantidade"] -= quantidade

        if produtos[indice]["Quantidade"] == 0:
            produtos.pop(indice)

        salvar_produtos(produtos)
        listar_produtos()
        while True:
            entrada = input("Deseja retirar mais algum produto? (s/n): ").strip().lower()

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
                print("⚠️ Entrada inválida! Digite apenas 's' para sim ou 'n' para não.")

#retirada_produtos()