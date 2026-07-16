import produtos
import interface

def iniciar():
    
    lista_produto = []

    produtos.adicionar_produto(lista_produto, produtos.cadastrar_produto("arroz", 17, 2))
    produtos.adicionar_produto(lista_produto, produtos.cadastrar_produto("feijao", 7, 1))
    produtos.adicionar_produto(lista_produto, produtos.cadastrar_produto("linguiça", 10, 3))

    interface.menu(lista_produto)
    interface.exibir_produtos(lista_produto)

if __name__ == "__main__":
    iniciar()
