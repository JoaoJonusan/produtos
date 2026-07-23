
class Estoque():
    
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def buscar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto.casefold():
                return produto
        return None
    
    def remover_produto(self, nome_produto):
        produto_remove = self.buscar_produto(nome_produto)
        if produto_remove is None:
            return False
        self.produtos.remove(produto_remove)
        return True
    
    def quantidade_produtos(self):
        return len(self.produtos)
    
    def calcular_quantidade_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.quantidade
        return total
    
    def calcular_valor_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_valor_estoque()
        return total
    
    