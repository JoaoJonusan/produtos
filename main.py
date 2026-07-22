from app import produtos
from app import interface
from app import arquivos
from app.modelos import Produto

def iniciar():
    
    lista_produto = arquivos.carregar_produtos()
    '''
    interface.menu(lista_produto)
    interface.exibir_produtos(lista_produto)
    arquivos.salvar_produtos(lista_produto)
    
    '''
    
    print(lista_produto)
    produto = Produto.de_dicionario(lista_produto)
    
    print(produto)
 
if __name__ == "__main__":
    iniciar()
