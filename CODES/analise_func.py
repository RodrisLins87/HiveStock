import json
from datetime import datetime, timedelta
from utilits import limpar_tela, arquivo_mov   


def funcionario_mais_usou():
    try:
        with open(arquivo_mov, "r", encoding="utf-8") as f:
            movimentos = json.load(f)
    except:
        print("Nenhuma movimentação registrada.")
        return
    
    hoje = datetime.now()
    semana_atras = hoje - timedelta(days=7)

    # contador geral por funcionário {usuario: total_unidades}
    uso = {}

    # contador de produtos por funcionário {usuario: {produto: unidades}}
    produtos_por_usuario = {}

    for mov in movimentos:
        # Só conta retiradas
        if mov.get("tipo") != "saida":
            continue

        # Converter data
        data_mov = datetime.strptime(mov["data"], "%d/%m/%Y %H:%M")

        # Se é da última semana
        if data_mov >= semana_atras:
            usuario = mov["usuario"]
            produto = mov["nome"]
            quant = mov["quantidade"]

            # Soma total retirado pelo funcionário
            uso[usuario] = uso.get(usuario, 0) + quant

            # Soma por produto que o funcionário retirou
            if usuario not in produtos_por_usuario:
                produtos_por_usuario[usuario] = {}

            produtos_por_usuario[usuario][produto] = (
                produtos_por_usuario[usuario].get(produto, 0) + quant
            )

    if not uso:
        print("Nenhum produto foi usado na última semana.")
        return

    # Funcionário que mais retirou unidades
    mais_usou = max(uso, key=uso.get)

    # Produto mais usado pelo funcionário
    produtos_do_func = produtos_por_usuario[mais_usou]
    produto_top = max(produtos_do_func, key=produtos_do_func.get)
    qtd_produto_top = produtos_do_func[produto_top]

    print("\n📊 **ANÁLISE DA SEMANA**")
    print("========================================")
    print(f"➡ Funcionário que mais retirou: {mais_usou}")
    print(f"➡ Total de unidades retiradas: {uso[mais_usou]}")
    print("----------------------------------------")
    print("📌 Produto mais retirado por ele:")
    print(f"➡ {produto_top} — {qtd_produto_top} unidades")
    print("========================================")

    input("\nPressione ENTER para sair...")
    limpar_tela()

funcionario_mais_usou()