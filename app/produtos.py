
def cadastrar_produto(nome, preco, quantidade):    
    return {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    
def adicionar_produto(lista, produto):
    lista.append(produto)
    
def remover_produto(lista, nome_produto):
    produto = buscar_produto(lista, nome_produto)

    if produto is None:
        return False

    lista.remove(produto)
    return True

def atualizar_produto(lista, nome_produto, novo_preco):
    produto = buscar_produto(lista, nome_produto)
    
    if produto is None:
        return False
    
    produto["preco"] = novo_preco
    return True

def buscar_produto(lista, nome_produto):
    for produto in lista:
        if produto["nome"].lower() == nome_produto.lower():
            return produto

    return None

def calcular_quantidade_total(lista):
    total_quantidade = 0
    for produto in lista:
        total_quantidade += produto["quantidade"]
    return total_quantidade

def calcular_valor_total_estoque(lista):
    valor_total = 0
    for produto in lista:
        valor_total += calcular_valor_estoque(produto)
    return valor_total

def calcular_valor_estoque(produto):
    return produto["preco"] * produto["quantidade"]
