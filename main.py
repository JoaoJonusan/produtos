from app import produtos
from app import interface
from app import arquivos

def iniciar():
    
    lista_produto = arquivos.carregar_produtos()

    interface.menu(lista_produto)
    interface.exibir_produtos(lista_produto)
    
    arquivos.salvar_produtos(lista_produto)

if __name__ == "__main__":
    iniciar()
