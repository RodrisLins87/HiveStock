import json
from datetime import datetime, timedelta
from utilits import aguardar,limpar_tela, arquivo_mov   


def produto_mais_usado_semana():
    try:
        with open(arquivo_mov, "r") as f:
            movimentos = json.load(f)
    except:
        print("Nenhuma movimentação registrada.")
        return
    
    hoje = datetime.now()
    semana_atras = hoje - timedelta(days=7)

    # contador {nome: quantidade_saida}
    uso = {}

    for mov in movimentos:
        if mov["tipo"] != "saida":
            continue

        data_mov = datetime.strptime(mov["data"], "%d/%m/%Y %H:%M")

        if data_mov >= semana_atras:
            nome = mov["nome"]
            quant = mov["quantidade"]
            uso[nome] = uso.get(nome, 0) + quant

    if not uso:
        print("Nenhum produto foi usado na última semana.")
        return

    # pega o mais usado
    mais_usado = max(uso, key=uso.get)

    print("\n📊 **PRODUTO MAIS USADO DA SEMANA**")
    print(f"Produto: {mais_usado}")
    print(f"Quantidade retirada: {uso[mais_usado]}")

    entrada = input("\nPressione ENTER para sair...")
    if entrada == "":
        limpar_tela()
        return  

#produto_mais_usado_semana()