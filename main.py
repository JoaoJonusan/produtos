from app import produtos
from app import interface
from app import arquivos
from app.modelos import Produto

def iniciar():
    
    lista_produto = arquivos.carregar_produtos()

    interface.menu(lista_produto)
    interface.exibir_produtos(lista_produto)
    arquivos.salvar_produtos(lista_produto)
    
    '''produto1 = Produto('',22, 1)
    produto2 = Produto('pao',-8, 2)
    produto3 = Produto('feijao',2, 1)
    print(produto1.nome)
    print(produto2.nome)
    print(produto3.nome)'''

if __name__ == "__main__":
    iniciar()
