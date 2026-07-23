from app import produtos
from app import interface
from app import arquivos
from app.modelos import Produto
from app.perecivel import Produto_perecivel
from app.estoque import Estoque

def iniciar():
    
    lista_produto = arquivos.carregar_produtos()
    '''
    interface.menu(lista_produto)
    interface.exibir_produtos(lista_produto)
    arquivos.salvar_produtos(lista_produto)
    
    
    lista = []
    
    produto1 = Produto('arroz', 25, 2)
    produto2 = Produto('feijao', 17, 1)
    produto3 = Produto_perecivel('leite', 25, 2,'27/08/26')
    produto4 = Produto('macarrao', 10, 4)
    lista.append(produto1)
    lista.append(produto2)
    lista.append(produto3)
    lista.append(produto4)
    
    for produto in lista:
        print(produto.descricao())
    '''
    
    estoque = Estoque()

    arroz = Produto("arroz", 17, 2)

    leite = Produto_perecivel(
        "leite",
        6.50,
        10,
        "30/07/2026"
    )

    estoque.adicionar_produto(arroz)
    estoque.adicionar_produto(leite)

    print(estoque.buscar_produto("ARROZ"))
    print(estoque.quantidade_produtos())
    print(estoque.calcular_quantidade_total())
    print(estoque.calcular_valor_total())

    print(estoque.remover_produto("leite"))
    print(estoque.quantidade_produtos())
 
if __name__ == "__main__":
    iniciar()
