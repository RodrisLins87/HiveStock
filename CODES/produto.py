# ============================================
#   CLASSE PRODUTO
# ============================================

class Produto:
    def __init__(self, tipo, nome_produto, quantidade, nota_fiscal, data_atual, mes_ano):
        self.tipo = tipo
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.nota_fiscal = nota_fiscal
        self.data_atual = data_atual
        self.mes_ano = mes_ano

    def to_dict(self):
        return {
            "Tipo": self.tipo,
            "Nome": self.nome_produto,
            "Quantidade": self.quantidade,
            "NF": self.nota_fiscal,
            "data_inclusao": self.data_atual,
            "mes_ano": self.mes_ano
        }
