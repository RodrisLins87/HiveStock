from CODES.utilits import aguardar,limpar_tela, arquivo_mov
from CODES.cadastro_de_produtos import listar_produtos, carregar_produtos,salvar_produtos
import json
from datetime import datetime



def registrar_movimentacao(nome, quantidade, tipo, nome_usuario):
    try:
        with open(arquivo_mov, "r") as f:
            movs = json.load(f)
    except:
        movs = []

    movs.append({
        "nome": nome,
        "quantidade": quantidade,
        "tipo": tipo,               # "entrada" ou "saida"
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "usuario": nome_usuario
    })

    with open(arquivo_mov, "w") as f:
        json.dump(movs, f, indent=4)


def adicionar_quantidade_prod(nome_usuario):
    produtos = carregar_produtos()
    
    while True:
        if not produtos:
            print("Não existem produtos cadastrados.")
            return

        while True:
            try:
                listar_produtos()

                print("\n(Para cancelar, digite 0)")
                print("Digite o indice do produto que você quer retirar")
                indice = int(input())-1
                comprimento = len(produtos)
                if indice < -1 or indice+1 > comprimento:
                    limpar_tela()
                    print(f"⚠️ Digite um valor valido. Não serão aceitos numeros maiores que {comprimento} ⚠️")
                    continue
                elif indice == -1:
                    return
            except ValueError:
                limpar_tela()
                print("⚠️ Digite um valor valido. Só serão aceitos numeros ⚠️")
                continue
            break

        aguardar(2)
        limpar_tela()
        
        while True:
            try:       
                print("\n(Para cancelar, digite 0)")
                quantidade = int(input("Digite a quantidade a ser adicionada\n"))
                if quantidade < 0 or quantidade > 500:
                    limpar_tela()
                    print("⚠️ Digite um valor valido. Numeros negativos não serão aceitos, nem valores superiores a 500 ⚠️")
                    continue
                elif quantidade == 0:
                    return
            except ValueError:
                limpar_tela()
                print("⚠️ Digite um valor valido. Só serão aceitos numeros ⚠️")
                continue
            break

        print("Aguarde...")
        aguardar(2)
        limpar_tela()

        produtos[indice]["Quantidade"] += quantidade

    
        salvar_produtos(produtos)
        listar_produtos()
        
        registrar_movimentacao(produtos[indice]["Nome"], quantidade, "entrada", nome_usuario)

        
        aguardar(2)
        

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
                limpar_tela()
                continue

def retirada_produtos(nome_usuario):
    produtos = carregar_produtos()
    
    while True:
        if not produtos:
            print("Não existem produtos cadastrados.")
            return

        while True:
            try:
                listar_produtos()

                print("\n(Para cancelar, digite 0)")
                print("Digite o indice do produto que você quer retirar")
                indice = int(input())-1
                comprimento = len(produtos)
                if indice < -1 or indice+1 > comprimento:
                    limpar_tela()
                    print(f"⚠️ Digite um valor valido. Não serão aceitos numeros maiores que {comprimento} ⚠️")
                    continue
                elif indice == -1:
                    return
            except ValueError:
                limpar_tela()
                print("⚠️ Digite um valor valido. Só serão aceitos numeros ⚠️")
                continue
            break

        aguardar(2)
        limpar_tela()
        
        while True:
            try:       
                print("\n(Para cancelar, digite 0)")
                quantidade = int(input("Digite a quantidade a ser retirada\n"))
                if quantidade < 0 or quantidade > produtos[indice]["Quantidade"]:
                    limpar_tela()
                    print("⚠️ Digite um valor valido. Numeros negativos não serão aceitos, nem um valor superior a quantidade atual. ⚠️")
                    continue
                elif quantidade == 0:
                    return
            except ValueError:
                limpar_tela()
                print("⚠️ Digite um valor valido. Só serão aceitos numeros ⚠️")
                continue
            break

        print("Aguarde...")
        aguardar(2)
        limpar_tela()

        produtos[indice]["Quantidade"] -= quantidade

        excluiu = False
        if produtos[indice]["Quantidade"] == 0:
            print(f"Foi retirado {quantidade} unidades de {produtos[indice]["Nome"]} do estoque")
            registrar_movimentacao(produtos[indice]["Nome"], quantidade, "saida", nome_usuario)
            produtos.pop(indice)
            excluiu = True
        else:
            print(f"Foi retirado {quantidade} unidades de {produtos[indice]["Nome"]} do estoque")

        salvar_produtos(produtos)
        listar_produtos()
        if not excluiu:
            registrar_movimentacao(produtos[indice]["Nome"], quantidade, "saida", nome_usuario)

        
        aguardar(2)
        

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
                limpar_tela()
                continue

#adicionar_quantidade_prod()
#retirada_produtos()
