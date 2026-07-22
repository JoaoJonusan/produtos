
class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    #Getter and Setter
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        novo_nome = novo_nome.strip()
        if not novo_nome:
            raise ValueError("O nome não pode ficar vazio!")
        self._nome = novo_nome
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero!")
        self._preco = novo_preco
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa!")
        self._quantidade = quantidade
    
    #metodos
    
    def calcular_valor_estoque(self):        
        return self.preco * self.quantidade
    
    def adicionar_estoque(self, quant):
        if quant <= 0:
            return False
        
        self.quantidade += quant
        return True

    def remover_estoque(self, quant):
        if quant <= 0 or quant > self.quantidade:
            return False

        self.quantidade -= quant
        return True
    
    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
    
    #Return String format
    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Preco: {self.preco} | "
            f"Quantidade: {self.quantidade}"
        )
    