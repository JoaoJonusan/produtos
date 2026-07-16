
def obter_preco(mensagem="Digite um preço: "):
    while True:
        try:
            preco = float(input(mensagem))

            if preco <= 0:
                print("O preço precisa ser maior que zero.")
            else:
                return preco

        except ValueError:
            print("Digite um valor numérico.")
            
def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Digite uma quantidade: "))

            if quantidade < 0:
                print("A quantidade nao pode ser negativa")
            else:
                return quantidade

        except ValueError:
            print("Digite um número inteiro.")
            
def obter_nome(mensagem="Nome: "):
    while True:
        nome = input(mensagem).strip()

        if not nome:
            print("O nome não pode ficar vazio.")
        else:
            return nome       
