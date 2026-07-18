
class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def calcular_valor_estoque(self):        
        return self.preco * self.quantidade
    
    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= 0 or quantidade > self.quantidade:
            return False

        self.quantidade -= quantidade
        return True