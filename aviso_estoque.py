import json
import time
import os
from datetime import datetime
from cadastro_de_produtos import listar_produtos, carregar_produtos,salvar_produtos

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def monitoramento():
    produtos = carregar_produtos()
    if not produtos:
        print("Não existem produtos cadastrados")
        return
    
    baixo_estoque = False
    
    for i,a in enumerate(produtos, start= 1):
        if a["Quantidade"] <= 10:
            baixo_estoque = True
            print(f"{i}. Tipo: {a["Tipo"]} | Nome: {a["Nome"]} | Quant: {a["Quantidade"]} | Nota fiscal: {a["NF"]}")
        
    if not baixo_estoque:
        print("✅ Todos os produtos estão com uma quantidade adequada em estoque.")


    entrada = input("Pressione ENTER para sair")
    if entrada == "":
        print("Saindo...")
        time.sleep(2)
        limpar_tela()
        return
    
