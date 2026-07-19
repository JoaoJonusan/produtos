
class Produto:

    def __init__(self, nome, preco, quantidade):
        if not nome.strip():
            raise ValueError("O nome nao pode ficar vazio")
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero")
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")

        self.nome = nome.strip()
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