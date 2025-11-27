from datetime import datetime
from estoqueTeste import Estoque
from produtoTeste import Produto
import json
import os

estoque = Estoque()  # usa o caminho universal automático


def teste_criar_produto_e_salvar():
    print("Criando produto de teste...")

    agora = datetime.now()

    p = Produto(
        codigo=9999,
        nome="Produto-Teste",
        categoria="Teste",
        quantidade=5,
        nf="NF-TESTE-9999",
        data=agora.strftime("%d/%m/%Y"),
        mes_ano=agora.strftime("%m-%Y")
    )

    estoque.cadastrar_produto(p)
    print("Produto salvo com sucesso!")


def mostrar_json_cru():
    print("\n📄 Conteúdo BRUTO do JSON:")

    if not os.path.exists(estoque.arquivo):
        print("⚠ Arquivo JSON não existe.")
        return

    with open(estoque.arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)
        print(json.dumps(dados, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    teste_criar_produto_e_salvar()
    estoque.visualizar_estoque()
    mostrar_json_cru()
