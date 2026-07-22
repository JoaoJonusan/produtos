from app import validacoes
from app import produtos
from app.modelos import Produto
def exibir_produto(produto):
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
        
def exibir_produtos(lista):
    if not lista:
        print("Nenhum produto cadastrado.")
        return
    
    for produto in lista:
        exibir_produto(produto)
        print("---------------")

def exibir_resumo_estoque(lista):
    total_produtos = len(lista)
    total_unidade = produtos.calcular_quantidade_total(lista)
    valor_total = produtos.calcular_valor_total_estoque(lista)
    
    print(f"Quantidade de produtos cadastrados: {total_produtos}")
    print(f"Quantidade total de unidades: {total_unidade}")
    print(f"Valor total do estoque: R${valor_total:.2f}")
    

def exibir_menu():
    opcoes = [
        "1 - Cadastrar",
        "2 - Listar",
        "3 - Remover",
        "4 - Buscar",
        "5 - Atualizar",
        "6 - Resumo",
        "7 - Sair"
    ]
    for opcao in opcoes:
        print(opcao)
            
def menu(lista_produto):    
    opcoes_validas = [1, 2, 3, 4, 5, 6, 7]

    while True:
        exibir_menu()
        try: 
            escolha = int(input("Faça sua escolha: "))
        except ValueError:
            print("valor incorreto")
            continue
            
        if escolha not in opcoes_validas:
            print("Escolha inexistente")
            continue
            
        if escolha == 1:
            nome = validacoes.obter_nome("Nome do produto: ")
            preco = validacoes.obter_preco("Preço do produto: ")
            quantidade = validacoes.obter_quantidade()
            produto = produtos.cadastrar_produto(nome, preco, quantidade)
            produtos.adicionar_produto(lista_produto, produto)
            print("Produto cadastrado com sucesso!")
            
        elif escolha == 2:
            exibir_produtos(lista_produto)
            
        elif escolha == 3:
            
            if not lista_produto:
                print("Nenhum produto cadastrado.")
                continue
            exibir_produtos(lista_produto)
            
            nome_produto = validacoes.obter_nome("Produto que deseja remover: ")
            if produtos.remover_produto(lista_produto, nome_produto):
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado")
                
        elif escolha == 4:
            nome_produto = validacoes.obter_nome("Produto que deseja buscar: ")

            resultado_busca = produtos.buscar_produto(lista_produto, nome_produto)

            if resultado_busca is not None:
                print("Produto encontrado:")
                exibir_produto(resultado_busca)
            else:
                print("Produto não encontrado.")
                
        elif escolha == 5:
            if not lista_produto:
                print("Nenhum produto cadastrado.")
                continue
            
            exibir_produtos(lista_produto)
            nome_produto = validacoes.obter_nome("Nome do produto a atualizar: ")
            novo_preco = validacoes.obter_preco("Digite o preço atualizado: ")
            
            if produtos.atualizar_produto(lista_produto, nome_produto, novo_preco):
                print('Valor alterado com sucesso')
            else:
                print('Produto não encontrado')
        elif escolha == 6:
            exibir_resumo_estoque(lista_produto)
            
        elif escolha == 7:
            return
