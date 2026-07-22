from app import produtos
from app import interface
from app import arquivos
from app.modelos import Produto

def iniciar():
    
    '''lista_produto = arquivos.carregar_produtos()

    interface.menu(lista_produto)
    interface.exibir_produtos(lista_produto)
    arquivos.salvar_produtos(lista_produto)
    
    '''
    produto1 = Produto('arroz',22, 1)
    produto2 = Produto('pao', 8, 2)
    produto3 = Produto('feijao',2, 1)

    
    print("-------------")
    
    try:
        produto1.preco = -25
    except ValueError as erro:
        print(erro)
    
if __name__ == "__main__":
    iniciar()
