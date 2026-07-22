from app.modelos import Produto

class Produto_perecivel(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade

    def __str__(self):
        texto_produto = super().__str__()
        return (
            f"{texto_produto} | "
            f"Data de validade: {self.data_validade}"
        )
