import json
import os
from produtoTeste import Produto

# Pega a pasta onde o arquivo está (CODES/)
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Vai para a raiz do projeto
ROOT = os.path.dirname(PASTA_ATUAL)

# Pasta Arquivos_JSON
PASTA_JSON = os.path.join(ROOT, "Arquivos_JSON")

# Caminho final do arquivo
CAMINHO_ESTOQUE = os.path.join(PASTA_JSON, "estoque.json")


class Estoque:
    def __init__(self, arquivo=CAMINHO_ESTOQUE):
        """
        Agora o Estoque usa corretamente o arquivo recebido.
        """
        self.arquivo = arquivo
        self.produtos = self.carregar()

    # ------------------ CARREGAR ------------------
    def carregar(self):
        if not os.path.exists(self.arquivo):
            return []

        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            return []

        lista = []
        for item in dados:
            lista.append(Produto(
                item["codigo"],
                item["nome"],
                item["categoria"],
                item["quantidade"],
                item["nf"],
                item["data"],
                item["mes_ano"]
            ))

        return lista

    # ------------------ SALVAR ------------------
    def salvar(self):
        # Garante que a pasta existe
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)

        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.produtos], f, indent=4, ensure_ascii=False)

    # ------------------ CADASTRAR ------------------
    def cadastrar_produto(self, produto: Produto):
        self.produtos.append(produto)
        self.salvar()
        return True

    # ------------------ VISUALIZAR ------------------
    def visualizar_estoque(self):
        if not self.produtos:
            print("\n⚠ Estoque vazio.\n")
            return

        print("\n===== ESTOQUE COMPLETO =====")
        for p in self.produtos:
            print(f"{p.codigo} | {p.nome} | {p.quantidade} unidades")

    # ------------------ BUSCAR ------------------
    def buscar_por_codigo(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p
        return None

    # ------------------ ATUALIZAR ------------------
    def atualizar_produto(self, codigo, novo_nome=None, nova_categoria=None):
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            print("Produto não encontrado.")
            return False

        if novo_nome:
            produto.nome = novo_nome
        if nova_categoria:
            produto.categoria = nova_categoria

        self.salvar()
        print("Produto atualizado!")
        return True

    # ------------------ EXCLUIR ------------------
    def excluir_produto(self, codigo):
        produto = self.buscar_por_codigo(codigo)

        if not produto:
            print("Produto não encontrado.")
            return False

        self.produtos.remove(produto)
        self.salvar()
        print("Produto removido!")
        return True
